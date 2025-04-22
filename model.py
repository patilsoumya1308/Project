import streamlit as st
import pandas as pd
from your_model import load_model, predict_branch  # Import your model functions

# Load the trained model
model = load_model()

# Streamlit UI
st.title("Engineering Branch Predictor")

# Input fields
jee_marks = st.number_input("Enter JEE Marks")
mht_cet_marks = st.number_input("Enter MHT-CET Marks")
twelve_marks = st.number_input("Enter 12th Grade Marks")
ten_marks = st.number_input("Enter 10th Grade Marks")
category = st.selectbox("Select Category", ["General", "OBC", "EWS"])

# Prediction button
if st.button("Predict"):
    input_data = pd.DataFrame({
        'JEE': [jee_marks],
        'MHT_CET': [mht_cet_marks],
        '12th': [twelve_marks],
        '10th': [ten_marks],
        'Category': [category]
    })
    prediction = predict_branch(model, input_data)
    st.success(f"Predicted Branch: {prediction}")
