from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('xgb_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    gender = request.form['gender']
    married = request.form['married']
    education = request.form['education']
    self_employed = request.form['self_employed']
    property_area = request.form['property_area']
    has_dependents = int(request.form['has_dependents'])

    # Numerical fields (convert string to float)
    applicant_income = float(request.form['applicant_income'])
    coapplicant_income = float(request.form['coapplicant_income'])
    loan_amount = float(request.form['loan_amount'])
    loan_term = float(request.form['loan_term'])
    credit_history = float(request.form['credit_history'])

    # Log transform & engineered features (same as training)
    applicant_income_log = np.log(applicant_income + 1)
    coapplicant_income_log = np.log(coapplicant_income + 1)
    loan_amount_log = np.log(loan_amount + 1)
    total_income = applicant_income + coapplicant_income
    debt_to_income = loan_amount / (total_income + 1)

    # Encode categoricals like in training
    gender = 1 if gender == 'Male' else 0
    married = 1 if married == 'Yes' else 0
    education = 1 if education == 'Graduate' else 0
    self_employed = 1 if self_employed == 'Yes' else 0
    property_area_dict = {'Urban': 2, 'Semiurban': 1, 'Rural': 0}
    property_area = property_area_dict.get(property_area, 0)

    # Final feature list (must match training order)
    input_features = np.array([[gender, married, education, self_employed,
                                applicant_income_log, coapplicant_income_log,
                                loan_amount_log, loan_term, credit_history,
                                total_income, debt_to_income,
                                property_area, has_dependents]])

    prediction = model.predict(input_features)[0]

    result = "Eligible ✅" if prediction == 1 else "Not Eligible ❌"
    return render_template('form.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
