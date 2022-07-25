from flask import Flask, render_template, request, flash, redirect
import pickle
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/diabetes", methods=['GET', 'POST'])
def diabetes():
    return render_template('diabetes.html')

@app.route("/breast_cancer", methods=['GET', 'POST'])
def breast_cancer():
    return render_template('breast_cancer.html')

@app.route("/heart", methods=['GET', 'POST'])
def heart():
    return render_template('heart.html')

@app.route("/kidney", methods=['GET', 'POST'])
def kidney():
    return render_template('kidney.html')

@app.route("/liver", methods=['GET', 'POST'])
def liver():
    return render_template('liver.html')

@app.route("/malaria", methods=['GET', 'POST'])
def malaria():
    return render_template('malaria.html')

@app.route("/pneumonia", methods=['GET', 'POST'])
def pneumonia():
    return render_template('pneumonia.html')

model_diabetes = pickle.load(open('Models/diabetes.pkl','rb'))
model_cancer = pickle.load(open('Models/breast_cancer.pkl','rb'))
model_heart = pickle.load(open('Models/heart.pkl','rb'))
model_kidney = pickle.load(open('Models/kidney.pkl','rb'))
model_liver = pickle.load(open('Models/liver.pkl','rb'))


@app.route("/diabetes_predict", methods = ['POST', 'GET'])
def predict_diabetes():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model_diabetes.predict(final_features)

    output = round(prediction[0], 1)

    if output == 1:
        result = "You have Diabetes, Please consult doctor"

    else:
        result = "You are Healthy!!"

    return render_template('diabetes.html', prediction_text=f'Prediction : {result}')

@app.route("/cancer_predict", methods = ['POST', 'GET'])
def predict_cancer():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model_cancer.predict(final_features)

    output = round(prediction[0], 1)

    if output == 1:
        result = "You have Breast Cancer, Please consult doctor"

    else:
        result = "You are Healthy!!"

    return render_template('breast_cancer.html', prediction_text=f'Prediction : {result}')

@app.route("/heart_predict", methods = ['POST', 'GET'])
def predict_heart():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model_heart.predict(final_features)

    output = round(prediction[0], 1)

    if output == 1:
        result = "You have Heart Disease, Please consult doctor"

    else:
        result = "You are Healthy!!"

    return render_template('heart.html', prediction_text=f'Prediction : {result}')

@app.route("/kidney_predict", methods = ['POST', 'GET'])
def predict_kidney():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model_kidney.predict(final_features)

    output = round(prediction[0], 1)

    if output == 1:
        result = "You have Kidney Disease, Please consult doctor"

    else:
        result = "You are Healthy!!"

    return render_template('kidney.html', prediction_text=f"Prediction : {result}")

@app.route("/liver_predict", methods = ['POST', 'GET'])
def predict_liver():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model_liver.predict(final_features)

    output = round(prediction[0], 1)

    if output == 1:
        result = "You have Liver Disease, Please consult doctor"

    else:
        result = "You are Healthy!!"

    return render_template('liver.html', prediction_text=f"Prediction : {result}")

if __name__ == '__main__':
	app.run()