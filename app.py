from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index_v2.html')

# Define the URL of the prediction API
PREDICTION_API_URL = "https://fish-prediction-eb8896516e03.herokuapp.com/predict"


@app.route("/predict", methods = ['GET', 'POST'])
def predict():
    weight = float(request.form.get("weight"))
    length1 = float(request.form.get("length1"))
    length2 = float(request.form.get("length2"))
    length3 = float(request.form.get("length3"))
    height = float(request.form.get("height"))
    width = float(request.form.get("width"))

    # Create the data payload for the POST request
    data = {
        "Weight": weight,
        "Lenght1": length1,
        "Lenght2": length2,
        "Lenght3": length3,
        "Height": height,
        "Width": width
    }

    # Send the POST request to the prediction API
    response = requests.post(PREDICTION_API_URL, json=data)

    if response.status_code == 200:
        prediction = response.json()["Predicted Species"]
    else:
        prediction = "Failed to get a prediction."

    return render_template("index_v2.html", predicted_species=prediction)   

if __name__ == '__main__':
    app.run()
