import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

st.title("🎓 Student Marks Prediction App")

st.sidebar.header("About Project")
st.sidebar.write("This app predicts student marks using Random Forest ML model.")

# -----------------------
# Load Dataset
# -----------------------
df = pd.read_csv("Exam_Score_Prediction.csv")

# Prepare Data
X = df.drop(["student_id", "exam_score"], axis=1)
y = df["exam_score"]

X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# -----------------------
# User Inputs
# -----------------------
age = st.number_input("Age", 15, 30)
gender = st.selectbox("Gender", ["male", "female", "other"])
course = st.selectbox("Course", ["b.tech", "bba", "bsc", "bca", "diploma"])
study_hours = st.number_input("Study Hours", 0, 12)
attendance = st.number_input("Class Attendance (%)", 0, 100)
internet_access = st.selectbox("Internet Access", ["yes", "no"])
sleep_hours = st.number_input("Sleep Hours", 0, 12)
sleep_quality = st.selectbox("Sleep Quality", ["poor", "average", "good"])
study_method = st.selectbox("Study Method", ["self-study", "group study", "coaching", "online videos"])
facility_rating = st.number_input("Facility Rating", 1, 5)
exam_difficulty = st.selectbox("Exam Difficulty", ["easy", "moderate", "hard"])

if st.button("Predict Marks"):

    input_data = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "course": [course],
        "study_hours": [study_hours],
        "class_attendance": [attendance],
        "internet_access": [internet_access],
        "sleep_hours": [sleep_hours],
        "sleep_quality": [sleep_quality],
        "study_method": [study_method],
        "facility_rating": [facility_rating],
        "exam_difficulty": [exam_difficulty]
    })

    input_data = pd.get_dummies(input_data)
    input_data = input_data.reindex(columns=X.columns, fill_value=0)

    prediction = model.predict(input_data)

    st.success(f"Predicted Marks: {prediction[0]:.2f}")
