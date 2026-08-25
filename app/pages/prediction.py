import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="EMIPredict AI - Prediction",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 EMI Prediction")
st.write(
    "Enter the applicant's personal and financial information "
    "to generate EMI predictions."
)

# ==============================
# LOAD TRAINED MODELS
# ==============================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

classification_model_path = os.path.join(
    BASE_DIR,
    "models",
    "emi_eligibility_model.pkl"
)

regression_model_path = os.path.join(
    BASE_DIR,
    "models",
    "max_emi_model.pkl"
)

classification_model = joblib.load(
    classification_model_path
)

regression_model = joblib.load(
    regression_model_path
)

# USER INPUT FORM

st.header("📋 Applicant Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=80,
        value=25
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    marital_status = st.selectbox(
        "Marital Status",
        ["Single", "Married"]
    )

    monthly_salary = st.number_input(
        "Monthly Salary (₹)",
        min_value=0.0,
        value=30000.0
    )

    years_of_employment = st.number_input(
        "Years of Employment",
        min_value=0.0,
        max_value=50.0,
        value=2.0
    )

    monthly_rent = st.number_input(
        "Monthly Rent (₹)",
        min_value=0.0,
        value=5000.0
    )

    family_size = st.number_input(
        "Family Size",
        min_value=1,
        max_value=20,
        value=4
    )

    dependents = st.number_input(
        "Number of Dependents",
        min_value=0,
        max_value=20,
        value=2
    )

    school_fees = st.number_input(
        "School Fees (₹)",
        min_value=0.0,
        value=0.0
    )

    college_fees = st.number_input(
        "College Fees (₹)",
        min_value=0.0,
        value=0.0
    )

with col2:
    travel_expenses = st.number_input(
        "Travel Expenses (₹)",
        min_value=0.0,
        value=3000.0
    )

    groceries_utilities = st.number_input(
        "Groceries & Utilities (₹)",
        min_value=0.0,
        value=8000.0
    )

    other_monthly_expenses = st.number_input(
        "Other Monthly Expenses (₹)",
        min_value=0.0,
        value=3000.0
    )

    existing_loans = st.number_input(
        "Existing Loans",
        min_value=0,
        max_value=10,
        value=0
    )

    current_emi_amount = st.number_input(
        "Current EMI Amount (₹)",
        min_value=0.0,
        value=0.0
    )

    credit_score = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=900,
        value=700
    )

    bank_balance = st.number_input(
        "Bank Balance (₹)",
        min_value=0.0,
        value=50000.0
    )

    emergency_fund = st.number_input(
        "Emergency Fund (₹)",
        min_value=0.0,
        value=10000.0
    )

    requested_amount = st.number_input(
        "Requested Loan Amount (₹)",
        min_value=0.0,
        value=300000.0
    )

    requested_tenure = st.number_input(
        "Requested Tenure (Months)",
        min_value=1,
        max_value=120,
        value=60
    )

# Additional categorical inputs

education = st.selectbox(
    "Education",
    ["Graduate", "High School", "Post Graduate", "Professional"]
)

employment_type = st.selectbox(
    "Employment Type",
    ["Salaried", "Self-Employed", "Business", "Contract"]
)

company_type = st.selectbox(
    "Company Type",
    ["Private", "Government", "MNC", "Other"]
)

house_type = st.selectbox(
    "House Type",
    ["Owned", "Rented", "Family"]
)

emi_scenario = st.selectbox(
    "EMI Scenario",
    [
        "Home Appliances EMI",
        "Personal Loan EMI",
        "Vehicle EMI",
        "Education EMI"
    ]
)

# PREPARE MODEL INPUT
# PREDICTION

if st.button("🔮 Predict EMI"):

    
    # INPUT VALIDATION
    
    errors = []

    if monthly_salary <= 0:
        errors.append("Monthly salary must be greater than 0.")

    if requested_amount <= 0:
        errors.append("Requested loan amount must be greater than 0.")

    if credit_score < 300 or credit_score > 900:
        errors.append("Credit score must be between 300 and 900.")

    if years_of_employment > age - 18:
        errors.append(
            "Years of employment cannot be greater than the possible working years."
        )

    if existing_loans == 0 and current_emi_amount > 0:
        errors.append(
            "Current EMI amount should be 0 when there are no existing loans."
        )

    # Stop if validation fails
    if errors:
        for error in errors:
            st.error(error)
        st.stop()
