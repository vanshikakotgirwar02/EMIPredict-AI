import streamlit as st

st.set_page_config(
    page_title="EMIPredict AI - About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About EMIPredict AI")

st.header("📌 Project Overview")

st.write(
    "EMIPredict AI is an end-to-end machine learning project "
    "that predicts EMI eligibility and maximum monthly EMI "
    "using applicant financial and personal information."
)

st.divider()

st.header("📊 Dataset")

st.write(
    "The dataset contains 404,800 records and 27 original "
    "features. After preprocessing and encoding, 44 features "
    "are used by the machine learning models."
)

st.divider()

st.header("🤖 Models Used")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Classification")
    st.write(
        "Predicts EMI eligibility as Eligible, High Risk, "
        "or Not Eligible."
    )

with col2:
    st.subheader("Regression")
    st.write(
        "Predicts the maximum monthly EMI amount."
    )

st.divider()

st.header("🛠️ Technologies Used")

st.write("""
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- Git & GitHub
""")

st.divider()

st.header("📁 Project Workflow")

st.write("""
Dataset
→ Data Exploration
→ Data Preprocessing
→ Model Training
→ Model Evaluation
→ Streamlit Application
→ Deployment
""")

st.divider()

st.header("👩‍💻 Project Author")

st.write("Vanshika Kotgirwar")

st.divider()

st.warning(
    "This application is developed for educational and "
    "demonstration purposes. Predictions should not be "
    "considered professional financial advice."
)