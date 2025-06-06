import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the trained model
model = joblib.load('model/random_forest.joblib')

def predict_status(inputs):
    prediction = model.predict(inputs)
    return prediction[0]

st.title("Jaya Institute App (Prototype)")

marital_status_mapping = {
    "Single": 1,
    "Maried": 2,
    "Widower": 3,
    "Divorced": 4,
    "Factounion": 5,
    "Legally separated": 6,
}

st.subheader('Identity Student')

col1, col2 = st.columns(2)
with col1:
    Gender = st.selectbox("Gender", ["Male", "Female"])
    gender_value = 1 if Gender == "Male" else 0
with col2:
    marital_status_label = st.selectbox("Marital Status", list(marital_status_mapping.keys()))
    Marital_value = marital_status_mapping[marital_status_label]
    
col1, col2 = st.columns(2)
with col1:
    Age = st.number_input("Age At Enrollment", min_value=17, max_value=70, value=17)
with col2:
    Tuition = st.selectbox("Tuition fees up to date", ["Yes", "No"])
    Tuition_value = 1 if Tuition == "Yes" else 0

col1, col2 = st.columns(2)
with col1:
    Admission_grade = st.number_input("Admission grade", min_value=95, max_value=190, value=95)
with col2:
    Scholarship_holder = st.selectbox("Scholarship Holder", ["Yes", "No"])
    Scholarship_holder_value = 1 if Scholarship_holder == "Yes" else 0

col1, col2 = st.columns(2)
with col1:
    Deptor = st.selectbox("Deptor", ["Yes", "No"])
    Deptor_value = 1 if Deptor == "Yes" else 0
with col2:
    Displaced = st.selectbox("Displaced", ["Yes", "No"])
    Displaced_value = 1 if Displaced == "Yes" else 0

st.subheader('Curricular Units 1st Semester')
col1, col2, col3, col4 = st.columns(4)
with col1:
    Enrolled_1 = st.number_input("1st sem Enrolled", min_value=0, max_value=26, value=0)
with col2:
    Grade_1 = st.number_input("1st sem grade", min_value=0.0, max_value=19.0, value=0.0, step=0.1)
with col3:
    Approved_1 = st.number_input("1st sem approved", min_value=0, max_value=26, value=0)
with col4:
    Evaluations_1 = st.number_input("1st sem evaluations", min_value=0, max_value=45, value=0)

st.subheader('Curricular Units 2nd Semester')
col1, col2, col3, col4 = st.columns(4)
with col1:
    Enrolled_2 = st.number_input("2nd sem enrolled", min_value=0, max_value=26, value=0)
with col2:
    Grade_2 = st.number_input("2nd sem grade", min_value=0.0, max_value=19.0, value=0.0, step=0.1)
with col3:
    Approved_2 = st.number_input("2nd sem approved", min_value=0, max_value=26, value=0)
with col4:
    Evaluations_2 = st.number_input("2nd sem evaluations", min_value=0, max_value=45, value=0)

# Simpan input user ke dictionary (untuk prediksi)
input_data = {
    "Marital_status": Marital_value,
    "Admission_grade": Admission_grade,
    "Displaced": Displaced_value,
    "Debtor": Deptor_value,
    "Tuition_fees_up_to_date": Tuition_value,
    "Gender": gender_value,
    "Scholarship_holder": Scholarship_holder_value,
    "Age_at_enrollment": Age,
    "Curricular_units_1st_sem_enrolled": Enrolled_1,
    "Curricular_units_1st_sem_evaluations": Evaluations_1,
    "Curricular_units_1st_sem_approved": Approved_1,
    "Curricular_units_1st_sem_grade": Grade_1,
    "Curricular_units_2nd_sem_enrolled": Enrolled_2,
    "Curricular_units_2nd_sem_evaluations": Evaluations_2,
    "Curricular_units_2nd_sem_approved": Approved_2,
    "Curricular_units_2nd_sem_grade": Grade_2,
}

input_df = pd.DataFrame([input_data])

with st.expander("View the Raw Data"):
    st.dataframe(input_df, width=800, height=10)

if st.button('Predict'):
    st.write("Status: {}".format(predict_status(input_df)))