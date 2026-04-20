import streamlit as st
import pandas as pd
import pickle

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Marks Prediction System",
    page_icon="🎓",
    layout="wide"
)

# ---------------- GRADIENT BACKGROUND ----------------
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #e3f2fd, #fce4ec);
    }

    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #1a237e;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: gray;
        margin-bottom: 30px;
    }

    .stButton>button {
        background: linear-gradient(to right, #667eea, #764ba2);
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        font-weight: bold;
    }

    .stButton>button:hover {
        background: linear-gradient(to right, #5a67d8, #6b46c1);
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="title">🎓 Student Marks Prediction System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Based Academic Performance Predictor</div>', unsafe_allow_html=True)

st.markdown("---")

# ---------------- SIDEBAR ----------------
st.sidebar.header("📘 About System")
st.sidebar.write("This system predicts student marks using Random Forest Machine Learning model.")
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
if st.button("🚀 Predict Marks"):

    # Create input dataframe
    input_data = pd.DataFrame([{
        "age": age,
        "gender": gender,
        "course": course,
        "study_hours": study_hours,
        "class_attendance": attendance,
        "sleep_hours": sleep_hours,
        "exam_difficulty": exam_difficulty
    }])

    # Convert categorical variables
    input_data = pd.get_dummies(input_data)

    # Match training columns
    input_data = input_data.reindex(columns=columns, fill_value=0)

    # Predict marks
    prediction = model.predict(input_data)
    predicted_marks = round(prediction[0], 2)

    st.markdown(f"""
        <div style="
            background: linear-gradient(to right, #d4fc79, #96e6a1);
            padding:25px;
            border-radius:15px;
            text-align:center;
            font-size:26px;
            font-weight:bold;
            color:#1b5e20;">
            📊 Predicted Marks: {predicted_marks}
        </div>
    """, unsafe_allow_html=True)