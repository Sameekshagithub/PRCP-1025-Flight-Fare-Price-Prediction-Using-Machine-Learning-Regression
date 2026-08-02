# Flight Fare Prediction (PRCP-1025)

A Flask web application that predicts flight ticket fares from booking
details (airline, source, destination, stops, journey date, timings, and
duration), using a Random Forest Regressor trained on historical flight
data. The frontend uses a minimal black-and-white theme.

## Project Structure

```
flight-fare-prediction/
├── app.py                 # Flask web application (backend + routes)
├── train_model.py         # Standalone training script
├── requirements.txt       # Python dependencies
├── data/
│   └── Flight_Fare.xlsx   # Training dataset
├── model/                 # Created by train_model.py
│   ├── flight_fare_model.pkl
│   ├── model_columns.pkl
│   └── dropdown_values.pkl
├── templates/
│   └── index.html         # Web form + result page
└── static/
    └── style.css           # Black & white styling
```

## Setup

1. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate         # Windows
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model:**

   ```bash
   python train_model.py
   ```

   This reads `data/Flight_Fare.xlsx`, cleans and engineers the features,
   trains a Random Forest Regressor, prints MAE / RMSE / R² on a held-out
   test set, and saves the model + supporting artifacts into `model/`.

4. **Run the web app:**

   ```bash
   python app.py
   ```

   Then open **http://127.0.0.1:5000/** in your browser.

## Using the App

Fill in the flight details on the form:

- Airline, Source, Destination
- Total Stops
- Journey Day / Month
- Departure Hour / Minute
- Arrival Hour / Minute
- Duration (in minutes)

Click **Predict Fare** to see the estimated ticket price.

## How It Works

- `train_model.py` mirrors the notebook pipeline: it loads the raw Excel
  data, drops missing/duplicate rows, extracts numeric date/time/duration
  features, ordinally encodes `Total_Stops`, one-hot encodes `Airline`,
  `Source`, and `Destination`, and trains a `RandomForestRegressor`.
- `app.py` loads the saved model and rebuilds a matching one-hot input
  row from the form data before calling `model.predict()`.
- The dropdown options on the form are generated directly from the
  categories the model was actually trained on, so the form and the
  model always stay in sync.

## Notes

- If you retrain the model on a different dataset, just delete the
  `model/` folder contents and re-run `train_model.py` — `app.py` will
  automatically pick up the new artifacts.
- `app.py` runs with `debug=True` for local development; turn this off
  before deploying anywhere public.
