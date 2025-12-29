# app.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib
import numpy as np
from scipy.sparse import hstack
from sklearn.metrics.pairwise import cosine_similarity
import warnings
from fastapi.middleware.cors import CORSMiddleware

# -------------------------------
# 1. Suppress warnings
# -------------------------------
warnings.filterwarnings("ignore")

# -------------------------------
# 2. Load bundle
# -------------------------------
bundle_path = "model/recommender_bundle.pkl"
bundle = joblib.load(bundle_path)

# -------------------------------
# 3. FastAPI setup
# -------------------------------
app = FastAPI(title="Career Recommendation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# 4. Templates setup
# -------------------------------
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# -------------------------------
# 5. Pydantic schema
# -------------------------------
class RecommendationRequest(BaseModel):
    keyword: str
    experience_months: int
    connections: int
    followers: int = 0
    avg_member_pos_duration: int = 0
    avg_company_pos_duration: int = 0

class RecommendationItem(BaseModel):
    career_step: str
    start_date: str
    end_date: str
    score: float

class RecommendationResponse(BaseModel):
    recommendations: list[RecommendationItem]

# -------------------------------
# 6. Endpoint UI
# -------------------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# -------------------------------
# 7. Endpoint API /recommend
# -------------------------------
@app.post("/recommend", response_model=RecommendationResponse)
def recommend(req: RecommendationRequest):
    keyword_vec = bundle['tfidf_vectorizer'].transform([req.keyword])
    numeric_input = np.array([[req.experience_months, 
                               req.connections, 
                               req.followers, 
                               req.avg_member_pos_duration, 
                               req.avg_company_pos_duration]])
                               
    numeric_vec = bundle['numeric_scaler'].transform(numeric_input)
    user_vec = hstack([keyword_vec, numeric_vec])
    similarity = cosine_similarity(user_vec, bundle['feature_matrix'])
    top_n = 20
    top_indices = similarity[0].argsort()[-top_n:][::-1]
    top_metadata = bundle['metadata'].iloc[top_indices]
    top_scores = similarity[0][top_indices]

    results = []
    for i, (_, row) in enumerate(top_metadata.iterrows()):
        results.append(RecommendationItem(
            career_step=row.get('career_step', 'Unknown'),
            start_date=str(row.get('startDateParsed', 'Unknown')),
            end_date=str(row.get('endDateParsed', 'Unknown')),
            score=round(float(top_scores[i])*100, 2)
        ))

    return RecommendationResponse(recommendations=results)
