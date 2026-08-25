import streamlit as st
import pandas as pd
import joblib
import os

# Page configuration
st.set_page_config(
    page_title="EMIPredict AI",
    page_icon="💰",
    layout="wide"
)

# ==============================
# SIDEBAR
# ==============================

with st.sidebar:
    st.header("💰 EMIPredict AI")

    st.write(
        "An AI-based system that predicts EMI eligibility "
        "and maximum affordable monthly EMI."
    )

    st.divider()

    st.subheader("How it works")

    st.write("1. Enter applicant details")
    st.write("2. Click Predict EMI")
    st.write("3. AI evaluates the applicant")
    st.write("4. View eligibility and maximum EMI")

    st.divider()

    st.caption("Machine Learning Project")

# Title
st.title("💰 EMIPredict AI")
st.subheader("AI-Based EMI Eligibility & Maximum EMI Prediction")

st.write(
    "Make smarter EMI decisions using machine learning."
)

st.write(
    "Enter the applicant's financial and personal details "
    "to predict EMI eligibility and maximum monthly EMI."
)

print("Application started successfully!")

# ==============================
# LOAD TRAINED MODELS
# ==============================

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model paths
classification_model_path = os.path.join(
    BASE_DIR, "models", "emi_eligibility_model.pkl"
)

regression_model_path = os.path.join(
    BASE_DIR, "models", "max_emi_model.pkl"
)

# Load models
classification_model = joblib.load(classification_model_path)
regression_model = joblib.load(regression_model_path)

st.success("Models loaded successfully!")

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

    
    # CREATE INPUT DATA
    
    input_data = pd.DataFrame([{
        "age": age,
        "gender": 1 if gender == "Male" else 0,
        "marital_status": 1 if marital_status == "Married" else 0,
        "monthly_salary": monthly_salary,
        "years_of_employment": years_of_employment,
        "monthly_rent": monthly_rent,
        "family_size": family_size,
        "dependents": dependents,
        "school_fees": school_fees,
        "college_fees": college_fees,
        "travel_expenses": travel_expenses,
        "groceries_utilities": groceries_utilities,
        "other_monthly_expenses": other_monthly_expenses,
        "existing_loans": existing_loans,
        "current_emi_amount": current_emi_amount,
        "credit_score": credit_score,
        "bank_balance": bank_balance,
        "emergency_fund": emergency_fund,
        "requested_amount": requested_amount,
        "requested_tenure": requested_tenure
    }])

    # Add categorical features
    input_data["education"] = education
    input_data["employment_type"] = employment_type
    input_data["company_type"] = company_type
    input_data["house_type"] = house_type
    input_data["emi_scenario"] = emi_scenario

    
    # ONE-HOT ENCODING
    
    categorical_columns = [
        "education",
        "employment_type",
        "company_type",
        "house_type",
        "emi_scenario"
    ]

    input_encoded = pd.get_dummies(
        input_data,
        columns=categorical_columns
    )

    
    # MATCH MODEL FEATURES
    
    expected_features = list(
        classification_model.feature_names_in_
    )

    for feature in expected_features:
        if feature not in input_encoded.columns:
            input_encoded[feature] = 0

    model_input = input_encoded[expected_features]


    # PREDICTIONS
   
    classification_prediction = classification_model.predict(
        model_input
    )[0]

    regression_prediction = regression_model.predict(
        model_input
    )[0]


    # DISPLAY RESULTS
    
    st.divider()

    st.header("📊 Prediction Results")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("EMI Eligibility")

        if classification_prediction == "Eligible":
            st.success("✅ Eligible")
        elif classification_prediction == "High_Risk":
            st.warning("⚠️ High Risk")
        else:
            st.error("❌ Not Eligible")

    with col2:
        st.subheader("Maximum Monthly EMI")

        st.metric(
            label="Recommended Maximum EMI",
            value=f"₹{regression_prediction:,.2f}"
        )

    st.info(
        "The predictions are generated using the trained machine "
        "learning models based on the information provided."
    )


# ABOUT

with st.expander("ℹ️ About EMIPredict AI"):
    st.write(
        "EMIPredict AI uses two machine learning models. "
        "The classification model predicts EMI eligibility, "
        "while the regression model predicts the maximum "
        "monthly EMI amount."
    )

    st.write(
        "The system is designed as a machine learning "
        "demonstration project and should not be used as "
        "the sole basis for real financial decisions."
    )