import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

import joblib

# Define the model variable outside the try block with an initial value of None
model = None

try:
    model = joblib.load(r'C:\Users\ASUS ZENBOOK\OneDrive\Bureau\Folder Requirement\modeel.pkl')
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading the model: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')  # Use the existing HTML template

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return "Model not loaded properly."

    # Retrieve form data
    year = int(request.form['Year'])
    present_price = float(request.form['Present_Price'])
    kms_driven = int(request.form['Kms_Driven'])

    # Create a feature vector based on the form data
    features = [year, present_price, kms_driven]

    # Perform prediction using your model here
    prediction = model.predict([features])

    return render_template('index.html', prediction_text=f'Predicted Selling Price: $ {prediction[0]:.2f}')

if __name__ == "__main__":
    app.run(debug=True)



# import numpy as np
# from flask import Flask, request, render_template

# app = Flask(__name__)

# import joblib

# try:
#     model = joblib.load(r'C:\Users\ASUS ZENBOOK\OneDrive\Bureau\Folder Requirement\modeel.pkl')
#     print("Model loaded successfully")
# except Exception as e:
#     print(f"Error loading the model: {str(e)}")

# @app.route('/')
# def index():
#     return render_template('index.html')  # Use the existing HTML template

# @app.route('/predict', methods=['POST'])
# def predict():
    
#     # Retrieve form data
#     year = int(request.form['Year'])
#     present_price = float(request.form['Present_Price'])
#     kms_driven = int(request.form['Kms_Driven'])
    
#     # Create a feature vector based on the form data
#     features = [year, present_price, kms_driven]

#     # Perform prediction using your model here
#     prediction = model.predict([features])

#     return render_template('index.html', prediction_text=f'Predicted Selling Price: $ {prediction[0]:.2f}')

# if __name__ == "__main__":
#     app.run(debug=True)

