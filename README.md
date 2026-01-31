# Prediksi Kelayakan Pinjaman: Proyek Klasifikasi End-to-End

Proyek ini bertujuan untuk membangun model Machine Learning yang dapat memprediksi apakah pengajuan pinjaman seorang nasabah akan disetujui atau tidak. Dengan menggunakan profil demografis dan finansial nasabah, model ini membantu mengotomatiskan proses pengambilan keputusan kredit.

## Gambaran Dataset
Dataset ini terdiri dari 614 baris data dengan 13 fitur utama yang mencakup informasi sebagai berikut:
* **Profil Demografis**: Gender, Status Pernikahan, Jumlah Tanggungan, dan Tingkat Pendidikan.
* **Informasi Finansial**: Pendapatan Pemohon, Pendapatan Pasangan, Jumlah Pinjaman, Jangka Waktu Pinjaman, dan Riwayat Kredit.
* **Target**: Status Pinjaman (Approved/Rejected).

## Alur Kerja Proyek

### 1. Pembersihan Data (Data Cleaning)
* **Penanganan Data Kosong**: Mengisi nilai yang hilang pada kolom numerik menggunakan **Median** dan kolom kategori menggunakan **Modus** (Mode).
* **Deteksi Pencilan**: Menggunakan Boxplot untuk mengidentifikasi outlier pada data pendapatan.
* **Label Encoding**: Mengonversi fitur kategorikal (teks) menjadi format numerik agar dapat diproses oleh algoritma machine learning.

### 2. Analisis Data Eksploratif (EDA)
* Melakukan visualisasi distribusi data untuk memahami profil mayoritas pemohon.
* Analisis korelasi antar variabel menggunakan Heatmap untuk melihat hubungan antara pendapatan dan jumlah pinjaman yang diajukan.

### 3. Rekayasa Fitur (Feature Engineering)
* **Transformasi Logaritma**: Menerapkan fungsi log untuk menormalisasi distribusi data yang miring (skewed) pada kolom pendapatan dan jumlah pinjaman.
* **Total Income**: Membuat fitur baru yang menggabungkan pendapatan pemohon dan pasangan untuk melihat gambaran kapasitas finansial secara keseluruhan.

### 4. Perbandingan Model
Eksperimen dilakukan menggunakan empat algoritma berbeda untuk mencari performa terbaik:

| Model | Akurasi |
| :--- | :--- |
| **Random Forest Classifier** | **77.9%** |
| Logistic Regression | 77.27% |
| Decision Tree | 72.73% |
| K-Nearest Neighbors (KNN) | 71.43% |

## 📈 Kesimpulan
Model **Random Forest Classifier** terpilih sebagai model terbaik karena menghasilkan akurasi tertinggi dibandingkan model lainnya. Model ini sangat efektif dalam mendeteksi calon nasabah yang layak mendapatkan pinjaman, yang dibuktikan dengan nilai Recall yang tinggi.

---
