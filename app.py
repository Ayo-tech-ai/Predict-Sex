import streamlit as st
import joblib

# Load your saved model
model = joblib.load('logistic_regression_model.pkl')

# Label mapping
label_mapping = {0: "Female", 1: "Male"}

# Define the prediction function
def predict_sex(input_data):
    prediction = model.predict([input_data])[0]  # Predict the class (0 or 1)
    return label_mapping[prediction]

# Streamlit App
st.title("Sex Prediction App")
st.write("This app predicts the sex of an individual based on their height and weight. Please provide the following information:")

# Input fields for height and weight
height = st.number_input("Height (in cm or as per your model)", min_value=0.0, step=0.1)
weight = st.number_input("Weight (in kg or as per your model)", min_value=0.0, step=0.1)

# Prediction button
if st.button("Predict"):
    # Prepare input data
    input_data = [height, weight]
    result = predict_sex(input_data)
    st.success(f"The predicted sex is: {result}")
