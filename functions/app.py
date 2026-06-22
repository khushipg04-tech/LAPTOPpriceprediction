import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd

print("Starting Flask App...")

app = Flask(__name__)

# Load model and encoder
laptop_model = pickle.load(open('laptop_model.pkl', 'rb'))
encoders = pickle.load(open('encoders.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('laptop.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.is_json:
        data = request.json.get('data', {})
        company = data.get('Company') or data.get('company')
        ram_val = data.get('Ram') or data.get('ram')
        weight_val = data.get('Weight') or data.get('weight')
    else:
        company = request.form.get('company')
        ram_val = request.form.get('ram')
        weight_val = request.form.get('weight')

    if not company or ram_val is None or weight_val is None:
        if request.is_json:
            return jsonify({'error': 'Missing required fields'}), 400
        else:
            return render_template('laptop.html', prediction_text="Error: Missing required inputs.")

    try:
        ram = float(ram_val)
        weight = float(weight_val)
    except ValueError:
        if request.is_json:
            return jsonify({'error': 'Invalid numerical values'}), 400
        else:
            return render_template('laptop.html', prediction_text="Error: RAM and Weight must be numbers.")

    # Encode company
    try:
        company_encoded = encoders['Company'].transform([company])[0]
    except ValueError:
        # Fallback if unknown company (e.g. default to Dell or first class)
        company_encoded = encoders['Company'].transform(['Dell'])[0]

    features = np.array([[company_encoded, ram, weight]])

    prediction = laptop_model.predict(features)[0]

    if request.is_json:
        return jsonify({
            'predicted_price': float(prediction)
        })
    else:
        prediction_text = f"Predicted Price: ₹{prediction:,.2f}"
        return render_template('laptop.html', prediction_text=prediction_text)

if __name__ == "__main__":
    print("Flask Server Running...")
    app.run(debug=True)