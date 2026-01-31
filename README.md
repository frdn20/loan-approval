# Loan Approval Prediction: An End-to-End Classification Project

Project ini bertujuan untuk membangun model machine learning yang dapat memprediksi kelayakan pinjaman nasabah secara otomatis. Menggunakan dataset profil nasabah, model ini mengklasifikasikan apakah pengajuan pinjaman akan disetujui (Approved) atau tidak (Rejected).

## Dataset Overview
[cite_start]Dataset ini berisi data dari 614 pemohon pinjaman dengan total 13 fitur kunci[cite: 45, 46]. [cite_start]Data dimuat dari file `dataset_loan_approval.csv` yang tersimpan di Google Drive[cite: 8].

Fitur-fitur utama meliputi:
* [cite_start]**Demografis**: Jenis Kelamin (Gender), Status Pernikahan (Married), Jumlah Tanggungan (Dependents), dan Pendidikan (Education)[cite: 100].
* [cite_start]**Finansial**: Pendapatan Pemohon (ApplicantIncome), Pendapatan Pasangan (CoapplicantIncome), Jumlah Pinjaman (LoanAmount), dan Riwayat Kredit (Credit_History)[cite: 100].
* [cite_start]**Target**: Status Pinjaman (Loan_Status)[cite: 100].

---

##  Langkah-Langkah Project

### 1. Data Cleaning & Preprocessing
Data awal ditemukan memiliki beberapa masalah yang harus diperbaiki sebelum masuk ke tahap modeling:
* [cite_start]**Missing Values**: Ditemukan data kosong pada kolom `Gender` (13), `Married` (3), `LoanAmount` (22), dan `Credit_History` (50)[cite: 105, 106, 113, 115].
* [cite_start]**Imputasi**: Kolom numerik diisi menggunakan nilai **Median**, sedangkan kolom kategori diisi menggunakan **Modus** (Mode)[cite: 140, 144, 145, 146, 147].
* [cite_start]**Outlier Handling**: Analisis menggunakan Boxplot menunjukkan adanya pencilan ekstrim pada kolom pendapatan[cite: 121, 122, 123].
* [cite_start]**Encoding**: Data teks (kategori) dikonversi menjadi format numerik menggunakan `LabelEncoder` agar dapat diolah oleh algoritma machine learning[cite: 502].

### 2. Exploratory Data Analysis (EDA)
Beberapa temuan penting dari analisis data awal:
* [cite_start]**Profil Dominan**: Mayoritas pemohon adalah laki-laki (502 orang) [cite: 172][cite_start], sudah menikah (401 orang) [cite: 190][cite_start], dan lulusan universitas (480 orang)[cite: 215].
* [cite_start]**Korelasi**: Terdapat korelasi positif sebesar **0.57** antara `ApplicantIncome` dan `LoanAmount`, yang menunjukkan bahwa jumlah pinjaman cenderung berbanding lurus dengan pendapatan[cite: 231, 232].

### 3. Feature Engineering
* [cite_start]**Log Transformation**: Untuk mengatasi kemiringan data (*skewness*) akibat outlier, diterapkan fungsi Logaritma (`np.log`) pada fitur pendapatan dan jumlah pinjaman[cite: 339, 357, 376, 390].
* [cite_start]**Total Income**: Membuat fitur baru `Total_Income` yang menggabungkan pendapatan pemohon dan pasangan untuk mendapatkan gambaran kemampuan bayar yang lebih akurat[cite: 270].

### 4. Performa Model
[cite_start]Saya melakukan uji coba terhadap empat algoritma klasifikasi yang berbeda[cite: 544, 545, 546, 547]. Berikut adalah hasil akurasinya:

| Algoritma | Akurasi (%) |
| :--- | :--- |
| **Random Forest Classifier** | [cite_start]**77%** [cite: 581] |
| Logistic Regression | [cite_start]77.27% [cite: 557] |
| Decision Tree | [cite_start]72.73% [cite: 566] |
| K-Nearest Neighbors (KNN) | [cite_start]71.43% [cite: 588] |

---

##  Kesimpulan
[cite_start]Berdasarkan eksperimen, model **Random Forest Classifier** memberikan hasil terbaik dengan akurasi tertinggi[cite: 581]. [cite_start]Model ini sangat efektif dalam mendeteksi nasabah yang layak (Recall kelas 1 mencapai 97%)[cite: 601], menjadikannya alat yang potensial untuk otomatisasi sistem persetujuan pinjaman.

---
