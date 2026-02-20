import streamlit as st
import pandas as pd
import pickle
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Marks Prediction",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1 style='text-align: center;'>🎓 Student Marks Prediction App</h1>", unsafe_allow_html=True)
st.markdown("---")

# ---------------- SIDEBAR ----------------
st.sidebar.header("📘 About Project")
st.sidebar.write("This app predicts student marks using Random Forest Machine Learning model.")
st.sidebar.write("Developed by Bhavesha Sakhare")

# ---------------- INPUT SECTION ----------------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 15, 30, 18)
    gender = st.selectbox("Gender", ["male", "female"])
    course = st.selectbox("Course", ["b.tech", "b.sc", "bca", "ba", "bba", "diploma"])
    study_hours = st.number_input("Study Hours", 0, 12, 4)

with col2:
    attendance = st.number_input("Class Attendance (%)", 0, 100, 75)
    sleep_hours = st.number_input("Sleep Hours", 0, 12, 7)
    exam_difficulty = st.selectbox("Exam Difficulty", ["easy", "moderate", "hard"])

st.markdown("---")

# ---------------- PREDICT BUTTON ----------------
if st.button("Predict Marks"):
    st.success("Predicted Marks: 95.20")  # Replace with actual prediction logic
    
