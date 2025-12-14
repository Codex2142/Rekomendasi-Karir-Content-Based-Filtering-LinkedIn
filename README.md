# Sistem Rekomendasi Jalur Karier Menggunakan Content-Based Filtering pada Dataset Profil LinkedIn

# 1. Identifikasi Masalah
Dataset LinkedIn Profiles and Jobs Data memiliki informasi profil, posisi, dan perusahaan, namun:
- Tidak tersedia label relevansi atau rating pekerjaan
- Tidak ada histori klik atau interaksi eksplisit
- Data bersifat heterogen (numerik, kategorikal, teks)  
**Masalah utama:**
Bagaimana membangun sistem rekomendasi pekerjaan yang tetap relevan tanpa ground truth, hanya berdasarkan kemiripan konten profil dan pekerjaan.


# 2. Tujuan Perencanaan
1. Tahap perencanaan bertujuan untuk:

2. Menentukan pendekatan sistem rekomendasi yang paling sesuai

3. Menentukan fitur yang digunakan dan perannya

4. Menyusun alur kerja (pipeline) yang terstruktur

5. Merancang pembagian notebook ```.ipynb ```agar:
- Mudah diuji
- Mudah dipahami
- Mudah dijalankan ulang oleh dosen

# 3. Metode yang digunakan
Berdasarkan karakteristik data:
- Tanpa rating/interaksi
- Profil & pekerjaan berbasis konten  

Metode yang dipilih:  
```Content-Based Recommendation System menggunakan Similarity Measurement```  
Alasan pemilihan:
- Tidak membutuhkan data historis pengguna lain
- Cocok untuk dataset statis
- Mudah dijelaskan secara akademik

# 4. Analisis & Seleksi Fitur (Planning Stage)
Pada tahap perencanaan, fitur diklasifikasikan dan direncanakan penggunaannya, belum diproses.

### 4.1 Fitur Teks (High Impact)
Digunakan untuk menangkap semantik pekerjaan:    
```mbrTitle```

```posTitle```

```companyName```

```posLocation```

Direncanakan untuk:  
- Digabung

- Diproses dengan TF-IDF


### 4.2 Fitur Numerik

```ageEstimate```

```connectionsCount```

```followersCount```

```companyFollowerCount```

```companyStaffCount```

```avgMemberPosDuration```

```avgCompanyPosDuration```

Direncanakan untuk:

- Normalisasi (scaling)

- Digabung dengan fitur teks

### 4.3 Fitur Kategorikal
Digunakan sebagai filter konteks:  
```country```

```posLocationCode```

```mbrLocationCode```  

Direncanakan untuk:  

- Encoding (One-Hot / Label Encoding)

### 4.4 Fitur yang Direncanakan Dihapus

```memberUrn```

```companyUrn```

```companyUrl```

```positionId```

```followable```

```companyHasLogo```

```hasPicture```

# 5. Perancangan Alur Sistem (System Workflow)

```sh
Dataset Mentah
   ↓
Seleksi & Klasifikasi Fitur
   ↓
Preprocessing Terpisah per Jenis Fitur
   ↓
Representasi Vektor
   ↓
Pengukuran Kemiripan
   ↓
Rekomendasi Top-N

```

### 5.1 Struktur Folder
```sh
Tubes/
│
├── dataset/
│   ├── raw/
│   │   └── dump.csv
│   └── cooked/
│       ├── cleaned_data.csv
│       ├── tfidf_vectorizer.pkl
│       ├── tfidf_matrix.pkl
│       ├── numeric_features.pkl
│       └── similarity_matrix.pkl
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_similarity_model.ipynb
│   ├── 05_recommendation_engine.ipynb
│   └── 06_evaluation_analysis.ipynb
│
├── web/
│   ├── app.py
│   ├── recommender.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── result.html
│   │   └── detail.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── main.js
│
└── README.md
```


# 6. Detail tiap File ```ipynb```
### ```01_data_understanding.ipynb```

Tujuan: Memahami data sebelum pemrosesan

Yang dilakukan:

    Load dataset

    Melihat struktur kolom

    Statistik deskriptif

    Analisis missing value

    Distribusi fitur numerik

Output: laporan pemahaman data

### ```02_data_preprocessing.ipynb```

Tujuan: Membersihkan dan menyiapkan data

Yang dilakukan:

    Drop fitur tidak relevan (sesuai perencanaan)

    Menangani missing value

    Standarisasi format teks

Simpan hasil:

```cleaned_data.csv```


### ```03_feature_engineering.ipynb```

Tujuan: Mengubah data menjadi vektor

Yang dilakukan:

    Gabung fitur teks

    TF-IDF Vectorization

    Scaling fitur numerik

    Encoding fitur kategorikal

    Gabungkan seluruh fitur

Simpan:

```tfidf_vectorizer.pkl```

```tfidf_matrix.pkl```

```numeric_features.pkl```


### ```04_similarity_model.ipynb```

Tujuan: Membangun model kemiripan

Yang dilakukan:

    Load feature matrix

    Hitung cosine similarity

Simpan:

```similarity_matrix.pkl```

### 05_recommendation_engine.ipynb

Tujuan: Membuat fungsi rekomendasi

Yang dilakukan:

    Load similarity matrix

    Buat fungsi recommend_jobs()

    Uji beberapa contoh profil

Validasi hasil secara logis

### 06_evaluation_analysis.ipynb
Tujuan: Evaluasi tanpa ground truth

Yang dilakukan:

    Analisis skor similarity

    Studi kasus manual

    Diskusi kekuatan & keterbatasan sistem

# 7. Implementasi Website
Arsitektur Website
```sh
<<<<<<< HEAD
1. preparation
2. feature engineering
3. similarity computation
4. ranking
5. implementasi final
6. output
```
=======
User (Browser)
   ↓
Flask Web UI
   ↓
Recommendation Engine (pickle model)
   ↓
Similarity Matrix
   ↓
Top-N Job Recommendation

```

### 7.1. Alur Kerja Website
1. User membuka halaman utama

2. User memilih atau mengisi profil

3. Flask memanggil engine rekomendasi

4. Sistem menghitung Top-N rekomendasi

5. Hasil ditampilkan di website


### 7.2. input pengguna  ```index.html```
Tujuan: Input data profil

Isi halaman:

- Dropdown / Input:

    - Job title saat ini

    - Lokasi

    - Negara

Estimasi umur

- Slider:

    - Jumlah koneksi

- Tombol:

    - “Cari Rekomendasi”

📌 Catatan:  
Tidak perlu semua fitur LinkedIn dimunculkan, cukup representatif.


### 7.3. Halaman Hasil rekomendasi ```result.html```
Tujuan: Menampilkan rekomendasi

Isi halaman:

- Daftar Top-5 / Top-10 pekerjaan

- Setiap rekomendasi menampilkan:

    - Job Title

    - Company Name

    - Location

    - Similarity Score (%)

- Tombol:

    - “Lihat Detail”


### 7.4. Halaman Detail ```detail.html```
Tujuan: Penjelasan kenapa direkomendasikan

Isi halaman:

- Profil input user

- Pekerjaan yang direkomendasikan

- Faktor kemiripan:

    - Judul pekerjaan

    - Lokasi

    - Perusahaan

    - Durasi posisi

### 7.5. Peran File Flask
```app.py```  
1. Routing Flask

2. Handling form input

3. Rendering HTML

```recommender.py```  
1. Load ```pkl```
2. Menjalankan  
```py
def recommend(user_input, top_n=5):
    ...
```

### 7.6. Integrasi File Model ke Flask (Alur Teknis)

1. Load file:

    - cleaned_data.csv

    - tfidf_vectorizer.pkl

    - tfidf_matrix.pkl

    - similarity_matrix.pkl

2. User input → vectorisasi:

    - TF-IDF untuk teks

    - Scaling numerik (jika digunakan)

3. Hitung similarity:

    - Cosine similarity user vs dataset

4. Ambil Top-N hasil
>>>>>>> 56ecddf26f957ec932f7456e4b2cc2e6e9111815
