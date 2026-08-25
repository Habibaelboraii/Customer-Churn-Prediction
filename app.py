import streamlit as st
import pandas as pd
import joblib

# =========================
# Load saved objects
# =========================
model = joblib.load("log_churn_model.pkl")
scaler = joblib.load("scaler.pkl")
encoders = joblib.load("encoders.pkl")

# =========================
# Page configuration
# =========================
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction")
st.write("Enter customer information to predict whether the customer is likely to churn.")

# =========================
# Helper function
# =========================
def encode_value(column, value):
    encoder = encoders[column]
    return encoder.transform([value])[0]


# =========================
# Customer Information
# =========================

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox(
        "Gender",
        encoders["gender"].classes_
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        encoders["Partner"].classes_
    )

    dependents = st.selectbox(
        "Dependents",
        encoders["Dependents"].classes_
    )

    tenure = st.number_input(
        "Tenure (months)",
        min_value=0.0,
        max_value=100.0,
        value=12.0
    )

    phone_service = st.selectbox(
        "Phone Service",
        encoders["PhoneService"].classes_
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        encoders["MultipleLines"].classes_
    )


with col2:
    internet_service = st.selectbox(
        "Internet Service",
        encoders["InternetService"].classes_
    )

    online_security = st.selectbox(
        "Online Security",
        encoders["OnlineSecurity"].classes_
    )

    online_backup = st.selectbox(
        "Online Backup",
        encoders["OnlineBackup"].classes_
    )

    device_protection = st.selectbox(
        "Device Protection",
        encoders["DeviceProtection"].classes_
    )

    tech_support = st.selectbox(
        "Tech Support",
        encoders["TechSupport"].classes_
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        encoders["StreamingTV"].classes_
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        encoders["StreamingMovies"].classes_
    )


with col3:
    contract = st.selectbox(
        "Contract",
        encoders["Contract"].classes_
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        encoders["PaperlessBilling"].classes_
    )

    payment_method = st.selectbox(
        "Payment Method",
        encoders["PaymentMethod"].classes_
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=1000.0
    )


# =========================
# Prediction
# =========================

if st.button("🔮 Predict Churn"):

    input_data = pd.DataFrame({
        "gender": [encode_value("gender", gender)],
        "SeniorCitizen": [senior_citizen],
        "Partner": [encode_value("Partner", partner)],
        "Dependents": [encode_value("Dependents", dependents)],
        "tenure": [tenure],
        "PhoneService": [encode_value("PhoneService", phone_service)],
        "MultipleLines": [encode_value("MultipleLines", multiple_lines)],
        "InternetService": [encode_value("InternetService", internet_service)],
        "OnlineSecurity": [encode_value("OnlineSecurity", online_security)],
        "OnlineBackup": [encode_value("OnlineBackup", online_backup)],
        "DeviceProtection": [encode_value("DeviceProtection", device_protection)],
        "TechSupport": [encode_value("TechSupport", tech_support)],
        "StreamingTV": [encode_value("StreamingTV", streaming_tv)],
        "StreamingMovies": [encode_value("StreamingMovies", streaming_movies)],
        "Contract": [encode_value("Contract", contract)],
        "PaperlessBilling": [encode_value("PaperlessBilling", paperless_billing)],
        "PaymentMethod": [encode_value("PaymentMethod", payment_method)],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges]
    })

    # Make sure columns are in the same order as training
    feature_order = [
        'gender',
        'SeniorCitizen',
        'Partner',
        'Dependents',
        'tenure',
        'PhoneService',
        'MultipleLines',
        'InternetService',
        'OnlineSecurity',
        'OnlineBackup',
        'DeviceProtection',
        'TechSupport',
        'StreamingTV',
        'StreamingMovies',
        'Contract',
        'PaperlessBilling',
        'PaymentMethod',
        'MonthlyCharges',
        'TotalCharges'
    ]

    input_data = input_data[feature_order]

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    # Probability
    probability = model.predict_proba(input_scaled)[0][1]

    st.divider()

    if prediction[0] == 1:
        st.error("⚠️ The customer is likely to churn.")
    else:
        st.success("✅ The customer is not likely to churn.")

    st.metric(
        "Churn Probability",
        f"{probability:.2%}"
    )