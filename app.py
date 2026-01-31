import streamlit as st
import pandas as pd
import numpy as np
import pickle

with open('best_model_rf.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🏦 Loan Approval Prediction App")
st.write("Aplikasi untuk memprediksi apakah pengajuan pinjaman Anda akan disetujui atau tidak.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
    married = st.selectbox("Status Pernikahan", ["Yes", "No"])
    dependents = st.selectbox("Jumlah Tanggungan", ["0", "1", "2", "3+"])
    education = st.selectbox("Pendidikan", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Wiraswasta", ["Yes", "No"])

with col2:
    applicant_income = st.number_input("Pendapatan Pemohon ($)", min_value=0)
    coapplicant_income = st.number_input("Pendapatan Pasangan ($)", min_value=0)
    loan_amount = st.number_input("Jumlah Pinjaman ($)", min_value=0)
    loan_term = st.number_input("Jangka Waktu Pinjaman (Hari)", min_value=0)
    credit_history = st.selectbox("Riwayat Kredit", [1.0, 0.0])
    property_area = st.selectbox("Area Properti", ["Urban", "Semiurban", "Rural"])

d_gender = 1 if gender == "Male" else 0
d_married = 1 if married == "Yes" else 0
d_education = 0 if education == "Graduate" else 1
d_self_employed = 1 if self_employed == "Yes" else 0

# Mapping Dependents & Property Area
dep_map = {"0": 0, "1": 1, "2": 2, "3+": 3}
d_dependents = dep_map[dependents]

prop_map = {"Rural": 0, "Semiurban": 1, "Urban": 2}
d_property_area = prop_map[property_area]

# Feature Engineering: Total Income & Log Transformation [cite: 270, 390]
total_income = applicant_income + coapplicant_income
total_income_log = np.log(total_income + 1)
applicant_income_log = np.log(applicant_income + 1)
loan_amount_log = np.log(loan_amount + 1)
loan_term_log = np.log(loan_term + 1)

# Gabungkan jadi array untuk prediksi
# Pastikan urutan kolom sama dengan X_train di notebook lo! [cite: 515]
features = np.array([[d_gender, d_married, d_dependents, d_education, d_self_employed, 
                      credit_history, d_property_area, applicant_income_log, 
                      loan_amount_log, loan_term_log, total_income_log]])

if st.button("Cek Kelayakan Pinjaman"):
    prediction = model.predict(features)
    
    st.subheader("Hasil Prediksi:")
    if prediction[0] == 1:
        st.success("✅ Selamat! Pengajuan Pinjaman Anda Kemungkinan Besar DISETUJUI.")
    else:
        st.error("❌ Mohon Maaf, Pengajuan Pinjaman Anda Kemungkinan DITOLAK.")


st.caption("Developed by Ferdian Hanif")
