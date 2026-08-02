"""
PRCP-1025 : Flight Fare Prediction
-----------------------------------
Standalone training script (VS Code / terminal version).

Loads data/Flight_Fare.xlsx, cleans it, engineers features, trains a
Random Forest Regressor, and saves the model + supporting artifacts
into the model/ folder so app.py can serve live predictions.

Run:
    python train_model.py
"""

import os
import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

DATA_PATH = os.path.join("data", "Flight_Fare.xlsx")
MODEL_DIR = "model"


def duration_to_minutes(duration: str) -> int:
    """Convert a duration string like '2h 50m' into total minutes."""
    duration = duration.strip()
    hours, minutes = 0, 0
    if "h" in duration:
        hours = int(duration.split("h")[0].strip())
        duration = duration.split("h")[1].strip()
    if "m" in duration:
        minutes = int(duration.replace("m", "").strip())
    return hours * 60 + minutes


def load_and_clean(path: str) -> pd.DataFrame:
    print(f"Loading dataset from {path} ...")
    df = pd.read_excel(path)
    print(f"Raw shape: {df.shape}")

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)
    print(f"Shape after cleaning: {df.shape}")
    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Date_of_Journey -> Journey_day / Journey_month
    df["Date_of_Journey"] = pd.to_datetime(df["Date_of_Journey"], format="%d/%m/%Y")
    df["Journey_day"] = df["Date_of_Journey"].dt.day
    df["Journey_month"] = df["Date_of_Journey"].dt.month
    df.drop("Date_of_Journey", axis=1, inplace=True)

    # Dep_Time -> Dep_hour / Dep_min
    df["Dep_hour"] = pd.to_datetime(df["Dep_Time"], format="%H:%M").dt.hour
    df["Dep_min"] = pd.to_datetime(df["Dep_Time"], format="%H:%M").dt.minute
    df.drop("Dep_Time", axis=1, inplace=True)

    # Arrival_Time -> Arrival_hour / Arrival_min (strip trailing date text if present)
    df["Arrival_Time"] = df["Arrival_Time"].apply(lambda x: x.split(" ")[0])
    df["Arrival_hour"] = pd.to_datetime(df["Arrival_Time"], format="%H:%M").dt.hour
    df["Arrival_min"] = pd.to_datetime(df["Arrival_Time"], format="%H:%M").dt.minute
    df.drop("Arrival_Time", axis=1, inplace=True)

    # Duration -> Duration_mins
    df["Duration_mins"] = df["Duration"].apply(duration_to_minutes)
    df.drop("Duration", axis=1, inplace=True)

    # Total_Stops -> ordinal number
    stops_map = {"non-stop": 0, "1 stop": 1, "2 stops": 2, "3 stops": 3, "4 stops": 4}
    df["Total_Stops"] = df["Total_Stops"].map(stops_map)

    # Drop high-cardinality / low-signal columns
    df.drop(["Route", "Additional_Info"], axis=1, inplace=True)

    return df


def encode_features(df: pd.DataFrame) -> pd.DataFrame:
    return pd.get_dummies(df, columns=["Airline", "Source", "Destination"], drop_first=True)


def main():
    os.makedirs(MODEL_DIR, exist_ok=True)

    df = load_and_clean(DATA_PATH)

    # Keep the raw category values before encoding, for the web form dropdowns
    airline_options = sorted(df["Airline"].unique().tolist())
    source_options = sorted(df["Source"].unique().tolist())
    destination_options = sorted(df["Destination"].unique().tolist())

    df = engineer_features(df)
    df_encoded = encode_features(df)

    X = df_encoded.drop(columns=["Price"])
    y = df_encoded["Price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Training Random Forest Regressor ...")
    model = RandomForestRegressor(
        n_estimators=120, max_depth=14, min_samples_leaf=2, random_state=42, n_jobs=-1
    )
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)

    print(f"MAE:  {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R2:   {r2:.4f}")

    # Recover the exact dropdown lists from the one-hot column names actually used
    # by the model (guards against any category that was dropped as the baseline).
    dropdown_values = {
        "Airline": sorted({c.replace("Airline_", "") for c in X.columns if c.startswith("Airline_")}),
        "Source": sorted({c.replace("Source_", "") for c in X.columns if c.startswith("Source_")}),
        "Destination": sorted({c.replace("Destination_", "") for c in X.columns if c.startswith("Destination_")}),
    }

    joblib.dump(model, os.path.join(MODEL_DIR, "flight_fare_model.pkl"))
    joblib.dump(list(X.columns), os.path.join(MODEL_DIR, "model_columns.pkl"))
    joblib.dump(dropdown_values, os.path.join(MODEL_DIR, "dropdown_values.pkl"))

    print(f"\nSaved model + artifacts to '{MODEL_DIR}/'.")
    print("You can now run: python app.py")


if __name__ == "__main__":
    main()
