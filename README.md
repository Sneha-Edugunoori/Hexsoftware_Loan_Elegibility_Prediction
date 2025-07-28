# 🧠 Loan Eligibility Prediction (ML Project)

This is a machine learning project where I learned and applied concepts from **data cleaning** to **model training**, and finally created a **Flask web app** that predicts whether a person is eligible for a loan.

---

## 👣 My Learning Journey

### 🔹 1. Data Cleaning
- Loaded the dataset using `pandas`
- Handled missing values in `LoanAmount`, `Self_Employed`, and `Credit_History`
- Encoded categorical values like `Gender`, `Education`, `Married`
- Applied **log transformation** to skewed features such as `ApplicantIncome` and `LoanAmount`

### 🔹 2. Feature Engineering
- Created new features:
  - `Total_Income = Applicant + Coapplicant`
  - `Debt_to_Income = LoanAmount / TotalIncome`
  - `Has_Dependents` as a binary field
- Used log scale for continuous fields to reduce skewness

### 🔹 3. Model Building
Tested the following ML algorithms:
- ✅ Logistic Regression
- ✅ Decision Tree
- ✅ Random Forest
- ✅ **XGBoost Classifier** *(Best accuracy)*

### 🔹 4. Model Evaluation
- Used `train_test_split` for data division (80% training, 20% testing)
- Evaluated with:
  - Accuracy Score
  - Confusion Matrix
  - Classification Report

---

## 🌐 Web App Using Flask

I built a simple UI using **Flask** where users can input loan application details and check loan eligibility instantly.

### 🔹 Input Fields:
- Gender
- Married
- Education
- Self Employed
- Property Area
- Dependents
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Term
- Credit History

### 🔹 Output:
<img width="346" height="80" alt="image" src="https://github.com/user-attachments/assets/026cff26-f037-43fb-b9c2-2d5588f4e054" />
<img width="415" height="169" alt="image" src="https://github.com/user-attachments/assets/d9d5b7f6-e34f-4f32-8d07-df37bf3ff020" />



---

## 🖼️ Project Visuals

👉 **Model Accuracy Comparison**  
*(Upload this image and paste its Markdown link below)*  
`![Model Accuracy](model_accuracy_comparison.png)`

👉 **XGBoost Classification Report**  
`![XGBoost Report](xgboost_classification_report.png)`

👉 **Precision / Recall / F1 Score**  
`![Metrics](metrics_table.png)`

📌 _To show these images on GitHub, just drag and drop them into this README while editing, or upload them and use the image URLs here._

---

## 🚀 How to Run This Project

```bash
# Step 1: Clone the repo
git clone https://github.com/your-username/loan-eligibility-prediction.git
cd loan-eligibility-prediction

# Step 2: Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run Flask app
python app.py

# Step 5: Visit in browser
http://localhost:5000

🛠 Tools & Tech Used
Python 🐍

Pandas, NumPy

Scikit-learn

XGBoost

Flask (for backend)

HTML & CSS (for frontend)

🙋‍♀️ Created By
Sneha Edugunoori
GitHub Profile


