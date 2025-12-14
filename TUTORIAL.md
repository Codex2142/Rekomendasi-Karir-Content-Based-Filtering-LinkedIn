# Cara Menjalankan Antarmuka Website
## 1. cek versi python
```sh
python --version
```
pastikan ada hasilnya:
```sh
python 3.10.19
```
## 2. membuat venv
kemudian buat venv dari python ```3.10.19```
```sh
py -3.10 -m venv recommender
```

nantinya akan tampil seperti dibawah ini
```sh
Tubes/
├── recommender/
│   ├── Scripts/
│   ├── Lib/
│   └── pyvenv.cfg
```

## 3. Run venv
buka terminal dan jalankan kode env yang baru saja dibuat
```sh
.\recommender\Scripts\Activate
```

tampilan bila berhasil menjalankan
```sh
(recommender) PS E:\Riwayat Kuliah\...
```

## 4. Unduh library yang dibutuhkan
jalankan perintah dengan terminal seperti dibawah ini:
```sh
pip install -r requirements.txt
```

## 5. jalankan ```app.py```
```sh
python run.py
```
kemudian akses link yang telah diberikan terminal
```sh
http://127.0.0.1:5000
```

# rangkuman
```sh
git clone https://github.com/Codex2142/Rekomendasi-Karir-Content-Based-Filtering-LinkedIn.git
cd Tubes
py -3.10 -m venv recommender
.\recommender\Scripts\activate
pip install -r requirements.txt
python run.py
```