"""
PRCP-1025 : Flight Fare Prediction
-----------------------------------
Flask frontend (VS Code / terminal version).

Loads the model trained by train_model.py and serves a simple
black-and-white web form for predicting flight fares.

Run:
    python app.py
Then open:
    http://127.0.0.1:5000/
"""

import os
from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

MODEL_DIR = "model"
MODEL_PATH = os.path.join(MODEL_DIR, "flight_fare_model.pkl")
COLUMNS_PATH = os.path.join(MODEL_DIR, "model_columns.pkl")
DROPDOWN_PATH = os.path.join(MODEL_DIR, "dropdown_values.pkl")

if not (os.path.exists(MODEL_PATH) and os.path.exists(COLUMNS_PATH) and os.path.exists(DROPDOWN_PATH)):
    raise FileNotFoundError(
        "Model artifacts not found in 'model/'. Run 'python train_model.py' first "
        "to train the model before starting the app."
    )

model = joblib.load(MODEL_PATH)
model_columns = joblib.load(COLUMNS_PATH)
dropdown_values = joblib.load(DROPDOWN_PATH)

STOPS_OPTIONS = [0, 1, 2, 3, 4]


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None
    form_values = {}

    if request.method == "POST":
        form_values = request.form.to_dict()
        try:
            airline = request.form.get("airline")
            source = request.form.get("source")
            destination = request.form.get("destination")
            total_stops = int(request.form.get("total_stops"))
            journey_day = int(request.form.get("journey_day"))
            journey_month = int(request.form.get("journey_month"))
            dep_hour = int(request.form.get("dep_hour"))
            dep_min = int(request.form.get("dep_min"))
            arrival_hour = int(request.form.get("arrival_hour"))
            arrival_min = int(request.form.get("arrival_min"))
            duration_mins = int(request.form.get("duration_mins"))

            # Build a single-row input vector matching the model's training columns
            input_df = pd.DataFrame(0, index=[0], columns=model_columns)

            input_df["Total_Stops"] = total_stops
            input_df["Journey_day"] = journey_day
            input_df["Journey_month"] = journey_month
            input_df["Dep_hour"] = dep_hour
            input_df["Dep_min"] = dep_min
            input_df["Arrival_hour"] = arrival_hour
            input_df["Arrival_min"] = arrival_min
            input_df["Duration_mins"] = duration_mins

            for prefix, value in [("Airline_", airline), ("Source_", source), ("Destination_", destination)]:
                col = f"{prefix}{value}"
                if col in input_df.columns:
                    input_df[col] = 1
                # if the chosen category was the encoding's dropped baseline category,
                # leaving all its dummy columns at 0 correctly represents it.

            predicted_price = model.predict(input_df)[0]
            prediction = round(float(predicted_price), 2)

        except Exception as exc:
            error = f"Could not generate a prediction: {exc}"

    return render_template(
        "index.html",
        airlines=dropdown_values["Airline"],
        sources=dropdown_values["Source"],
        destinations=dropdown_values["Destination"],
        stops_options=STOPS_OPTIONS,
        prediction=prediction,
        error=error,
        form_values=form_values,
    )


if __name__ == "__main__":
    app.run(debug=True)
