🧠 Loan Eligibility Prediction — ML Web App Project
This project helped me learn and apply the complete lifecycle of a machine learning model, right from data cleaning to deployment using Flask. It uses real-world loan data to predict whether a loan applicant is eligible or not, based on multiple input features.

👣 What I Learned in This Project
1️⃣ Data Preprocessing
Loaded dataset using pandas and explored it for missing or inconsistent values

Cleaned the dataset by filling null values (like LoanAmount, Self_Employed, Credit_History)

Converted categorical variables (e.g., Gender, Married, Education) into numerical format

Applied log transformation to skewed features like ApplicantIncome and LoanAmount

2️⃣ Feature Engineering
I created additional meaningful features to improve model performance:

Total_Income = ApplicantIncome + CoapplicantIncome

Debt_to_Income = LoanAmount / Total_Income

Created binary indicators like Has_Dependents

Applied log scaling to continuous fields for normalization

3️⃣ Model Building & Comparison
I experimented with different algorithms and compared their accuracy:

✅ Logistic Regression

✅ Random Forest Classifier

✅ XGBoost Classifier (Best performance)

4️⃣ Model Evaluation
Used train_test_split for splitting data

Evaluated models using:

Accuracy Score

Confusion Matrix

Classification Report (Precision, Recall, F1 Score)

🌐 Web App Interface using Flask
I built a web-based form using HTML + Flask backend to allow users to input loan details and get an instant prediction.

🔹 Input Fields
Gender

Married

Education

Self Employed

Applicant Income (log value)

Coapplicant Income (log value)

Loan Amount (log value)

Loan Term

Credit History

🔹 Output
Displays:

"Eligible ✅" or "Not Eligible ❌"
based on the prediction from the trained ML model

🚀 How to Run This Project
Clone this repository

Create a virtual environment

Install required packages:

nginx
Copy
Edit
pip install -r requirements.txt
Run the Flask app:

nginx
Copy
Edit
python app.py
Open your browser at:
http://localhost:5000

🛠 Tools & Technologies Used
Python

Pandas, NumPy

Scikit-learn

XGBoost

Flask

HTML & CSS

📂 Project Structure
bash
Copy
Edit
├── app.py                 # Flask backend
├── templates/
│   └── index.html         # Input form UI
├── loan_model.pkl         # Trained ML model (XGBoost)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
✅ Project Status
Model training completed ✔

Model deployed in Flask app ✔

Tested with multiple real-world inputs ✔

Ready to share for showcase ✔

🙋‍♀️ Created By
Sneha Edugunoori
GitHub Profile

