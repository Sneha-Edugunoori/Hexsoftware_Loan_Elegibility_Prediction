# 🧠 Loan Eligibility Prediction (ML Project)

This is a simple machine learning project where I learned and applied steps from **data cleaning** to **model building**, and finally created a **web app using Flask** to predict whether a person is eligible for a loan.

---

## 👣 My Learning Journey

### 1️⃣ Data Cleaning
- Loaded the loan dataset using `pandas`
- Handled missing values in columns like `LoanAmount`, `Self_Employed`, and `Credit_History`
- Converted categorical values (like Gender, Education) into numerical format
- Applied log transformation to skewed columns like `ApplicantIncome` and `LoanAmount`

### 2️⃣ Feature Engineering
- Created new features:
  - `Total_Income` = Applicant + Coapplicant income
  - `Debt_to_Income` = LoanAmount / TotalIncome
  - `Has_Dependents` as a binary feature
- Applied log scale to continuous fields to normalize them

### 3️⃣ Model Building
- Tried the following ML algorithms:
  - Logistic Regression
  - Random Forest
  - XGBoost Classifier ✅ (Best accuracy)

### 4️⃣ Model Evaluation
- Split data using `train_test_split`
- Evaluated using:
  - Accuracy score
  - Confusion matrix
  - Classification report

---

## 🌐 Web App using Flask

I used Flask to build a simple web interface where users can enter loan application details and check **eligibility**.

### 🔹 Input fields
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

### 🔹 Output
- Shows **"Eligible ✅"** or **"Not Eligible ❌"** based on the model prediction.

---

## 🚀 How to Run

1. Clone the repo
2. Create a virtual environment
3. Install dependencies using `pip install -r requirements.txt`
4. Run `app.py`
5. Open `http://localhost:5000` in your browser

---

## 🛠 Tools & Tech Used
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Flask (for web app)
- HTML & CSS (for frontend)

---

## 📂 Files Included
- `app.py` → Flask backend
- `form.html` → Input form UI
- `xgb_model.pkl` → Trained model
- `requirements.txt`
- `README.md`

---

## ✅ Project Status
✔ Model trained  
✔ Web app working  
✔ Tested with different inputs

---

## 🙋‍♀️ Created By
Sneha Edugunoori  
[GitHub Profile](https://github.com/Sneha-Edugunoori)

