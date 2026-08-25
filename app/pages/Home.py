import streamlit as st

st.set_page_config(
    page_title="EMIPredict AI",
    page_icon="💰",
    layout="wide"
)

st.title("💰 EMIPredict AI")
st.subheader("AI-Based EMI Eligibility & Maximum EMI Prediction")

st.write(
    "EMIPredict AI is a machine learning application that "
    "predicts EMI eligibility and estimates the maximum "
    "monthly EMI based on an applicant's financial profile."
)

st.divider()

st.header("🎯 Project Objective")

st.write(
    "The main objective of this project is to use machine learning "
    "to assist in evaluating an applicant's EMI eligibility and "
    "maximum affordable monthly EMI."
)

st.divider()

st.header("🔄 How the System Works")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("1️⃣ Input")
    st.write("Applicant provides personal and financial details.")

with col2:
    st.subheader("2️⃣ Processing")
    st.write("Input data is converted into the required model features.")

with col3:
    st.subheader("3️⃣ Prediction")
    st.write("Classification and regression models generate predictions.")

with col4:
    st.subheader("4️⃣ Result")
    st.write("The application displays EMI eligibility and maximum EMI.")

st.divider()

st.header("🤖 Machine Learning Models")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Classification Model")
    st.write(
        "Predicts the EMI eligibility category:"
    )
    st.write("• Eligible")
    st.write("• High Risk")
    st.write("• Not Eligible")

with col2:
    st.subheader("Regression Model")
    st.write(
        "Predicts the maximum monthly EMI amount "
        "that the applicant may be able to afford."
    )

st.divider()

st.info(
    "Use the Prediction page from the sidebar to enter applicant "
    "details and generate predictions."
)