from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load("acid_base.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        pH = float(request.form["pH"])
        hardness = float(request.form["hardness"])
        solids = float(request.form["solids"])
        conductivity = float(request.form["conductivity"])
        sulfate = float(request.form["sulfate"])

        input_data = np.array([[pH, hardness, solids, conductivity, sulfate]])
        result = model.predict(input_data)[0]

        prediction = "Basic" if result == 1 else "Acidic"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
