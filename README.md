# 💳 EMIPredict AI

An end-to-end Machine Learning project that predicts **EMI eligibility** and estimates the **maximum affordable monthly EMI** based on an applicant's financial and personal information.

The project includes data exploration, preprocessing, classification and regression model training, model evaluation, and a multi-page Streamlit web application for real-time predictions.

## 🚀 Live Demo

👉 https://emipredict-ai-g5wwrujzbwlqccvofrricm.streamlit.app

---

## 📌 Project Overview

EMIPredict AI is designed to assist in evaluating a person's EMI eligibility and estimating the maximum monthly EMI they can afford.

The system uses two Machine Learning models:

1. **Classification Model** – predicts EMI eligibility.
2. **Regression Model** – predicts the maximum monthly EMI amount.

The trained models are integrated into a **multi-page Streamlit application** that allows users to enter applicant information and receive predictions in real time.

---

## 🎯 Objectives

- Predict whether an applicant is eligible for EMI.
- Identify applicants as **Eligible, High Risk, or Not Eligible**.
- Estimate the maximum affordable monthly EMI.
- Build an interactive web application for real-time predictions.
- Evaluate the performance of both classification and regression models.
- Deploy the application using Streamlit Community Cloud.
- Maintain the complete project using GitHub and Git LFS.

---

## 📊 Dataset

The project uses an EMI prediction dataset containing **404,800 records and 27 original features**.

### Important Features

- Age
- Gender
- Marital Status
- Education
- Monthly Salary
- Employment Type
- Years of Employment
- Company Type
- House Type
- Monthly Rent
- Family Size
- Dependents
- School Fees
- College Fees
- Travel Expenses
- Groceries & Utilities
- Other Monthly Expenses
- Existing Loans
- Current EMI Amount
- Credit Score
- Bank Balance
- Emergency Fund
- EMI Scenario
- Requested Amount
- Requested Tenure

### Target Variables

#### Classification

`emi_eligibility`

Possible outcomes:

- Eligible
- High Risk
- Not Eligible

#### Regression

`max_monthly_emi`

This predicts the maximum monthly EMI amount an applicant can afford.

---

# 🔄 Project Workflow

```text
Dataset
   ↓
Data Exploration
   ↓
Data Preprocessing
   ↓
Feature Engineering
   ↓
Train/Test Split
   ↓
Classification Model Training
   ↓
Regression Model Training
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
Streamlit Application
   ↓
Real-Time Prediction
   ↓
Streamlit Cloud Deployment

EMIPredict_AI/
│
├── app/
│   ├── app.py
│   │
│   └── pages/
│       ├── Home.py
│       ├── prediction.py
│       └── About.py
│
├── data/
│   └── emi_prediction_dataset.csv
│
├── models/
│   ├── emi_eligibility_model.pkl
│   ├── max_emi_model.pkl
│   └── X_test.pkl
│
├── notebooks/
│   ├── 01_Data_Exploration.ipynb
│   ├── 02_Data_Preprocessing.ipynb
│   ├── 03_Model_Training.ipynb
│   └── 04_Model_Evaluation.ipynb
│
├── reports/
│   └── EMIPredict_AI_Project_Report.docx
│
├── requirements.txt
├── README.md
└── .gitignore

## 🔍 Data Exploration

The dataset was explored to understand its structure, quality, and important patterns.

### Key Steps
- Loaded the EMI prediction dataset using Pandas.
- Checked dataset shape, data types, and statistical summary.
- Analysed numerical and categorical features.
- Checked and handled missing values.
- Examined categorical value distributions.
- Analysed the target variables.
- Used visualizations to understand important feature relationships.

### Dataset
- **Records:** 404,800
- **Original Features:** 27
- **Classification Target:** `emi_eligibility`
- **Regression Target:** `max_monthly_emi`

---

## 🧹 Data Preprocessing

The data was prepared for Machine Learning by:

- Handling missing values.
- Cleaning inconsistent categorical values.
- Encoding categorical features using One-Hot Encoding.
- Separating features and target variables.
- Splitting the data into training and testing sets.
- Ensuring the same feature structure for classification and regression models.

After preprocessing, both models used **44 features**.

---

## 🤖 Model Training

Two Machine Learning models were developed.

### Classification

**Objective:** Predict EMI eligibility.

Target:

`emi_eligibility`

Classes:

- Eligible
- High Risk
- Not Eligible

**Algorithm:** Random Forest Classifier

Model file:

`models/emi_eligibility_model.pkl`

### Regression

**Objective:** Predict the maximum affordable monthly EMI.

Target:

`max_monthly_emi`

**Algorithm:** Random Forest Regressor

Model file:

`models/max_emi_model.pkl`

---

## 📊 Model Evaluation

The trained models were evaluated using test data.

### Classification Metrics
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

### Regression Metrics
- MAE
- MSE
- RMSE
- R² Score

The evaluation results were compared to determine the performance of both models.

---

## 🌐 Streamlit Application

A **multi-page Streamlit application** was developed for real-time predictions.

### Pages

**Home**
- Project overview
- Objectives
- ML workflow

**Prediction**
- Accepts applicant and financial details.
- Predicts EMI eligibility.
- Predicts maximum monthly EMI.

**About**
- Project information
- Technologies used
- Model details

### Prediction Workflow

```text
User Input
    ↓
Input Validation
    ↓
Feature Encoding
    ↓
Classification Prediction
    ↓
EMI Eligibility
    ↓
Regression Prediction
    ↓
Maximum Monthly EMI

☁️ Deployment

The application was deployed using Streamlit Community Cloud and connected to the GitHub repository.

Live Application:

https://emipredict-ai-g5wwrujzbwlqccvofrricm.streamlit.app

Large trained models are managed using Git LFS.

🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Streamlit
Git
GitHub
Git LFS

🚀 Key Features
EMI eligibility classification
Maximum monthly EMI prediction
Real-time predictions
Multi-page Streamlit UI
Input validation
Machine Learning model integration
Model evaluation
GitHub version control
Git LFS for large model files
Streamlit Cloud deployment
🔮 Future Improvements
Hyperparameter tuning
Improved model performance
Prediction probability display
Explainable AI
Interactive charts
Prediction history
Downloadable prediction reports
👩‍💻 Author

Vanshika Kotgirwar

Computer Science Engineering Student

📌 Live Application

EMIPredict AI – Streamlit App

