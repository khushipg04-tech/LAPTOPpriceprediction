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

    data = request.form['data']

    company = data['Company']
    ram = float(data['Ram'])
    weight = float(data['Weight'])

    # Encode company
    company_encoded = encoders['Company'].transform([company])[0]

    features = np.array([[company_encoded, ram, weight]])

    prediction = laptop_model.predict(features)[0]

    return jsonify({
        'predicted_price': float(prediction)
    })

if __name__ == "__main__":
    print("Flask Server Running...")
    app.run(debug=True)