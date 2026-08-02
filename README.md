# PRCP-1025: Flight Fare Prediction Using Machine Learning

A single Jupyter Notebook capstone project that analyzes historical flight
booking data, builds and compares multiple regression models to predict
flight ticket prices, and deploys the best model behind a black-and-white
Flask web frontend — all inside one notebook.

## File

- `PRCP-1025-FlightFarePrediction.ipynb` — the complete notebook (run top to bottom)

## Requirements

- **Dataset:** `Flight_Fare.xlsx` must be in the same folder as the notebook
- **Python packages:**

  ```bash
  pip install numpy pandas matplotlib seaborn scikit-learn joblib flask openpyxl
  ```

## How to Run

1. Place `Flight_Fare.xlsx` in the same directory as the notebook.
2. Open the notebook in Jupyter Notebook, JupyterLab, or VS Code.
3. Run all cells in order (`Run All` / `Kernel → Restart & Run All`).
4. The notebook trains, evaluates, and saves the model automatically —
   no manual steps needed until you want to launch the web app (see below).

## What's Inside

| Section | What it covers |
|---|---|
| 1 | Problem Statement & Project Objective |
| 2 | Import Python Libraries |
| 3 | Upload the Dataset & Domain Analysis |
| 4 | Basic Checks (shape, dtypes, missing values, duplicates) |
| 5 | Exploratory Data Analysis — Task 1 (distributions, bivariate analysis, outliers, correlation) |
| 6 | Data Preparation — feature engineering (date/time/duration parsing, encoding) + train/test split |
| 7 | Model Building — Linear Regression, Decision Tree, Random Forest, KNN, SVR, Gradient Boosting |
| 8 | Hyperparameter Tuning (GridSearchCV on Random Forest) |
| 9 | Model Comparison Report (MAE / MSE / RMSE / R² table + charts) |
| 10 | Feature Importance (Random Forest) |
| 11 | Model Testing on a new flight booking |
| 12 | Business Insights — Task 3 |
| 13 | Challenges Faced & Techniques Used |
| 14 | Final Conclusion |
| 15 | Model Deployment — saves the trained model with `joblib` |
| 16 | Flask Web Application — generates `app.py`, `templates/index.html`, `static/style.css` |
| 17 | Project Links (add your own GitHub/Drive links) |

## Launching the Web App (Optional)

Sections 15–16 write out a small Flask project (`app.py`, `templates/`,
`static/`) into the same folder as the notebook, plus the trained model
artifacts (`flight_fare_model.pkl`, `model_columns.pkl`,
`dropdown_values.pkl`). To try the live prediction form:

1. Run the notebook fully at least once (so the files above exist).
2. From a terminal, in that same folder:

   ```bash
   python app.py
   ```

3. Open **http://127.0.0.1:5000/** in your browser.
4. Enter airline, source, destination, stops, journey date, timings, and
   duration, then click **Predict Fare** to see the estimated price on
   the black-and-white themed page.

Flask runs a blocking server, so it must be started from a terminal —
not from inside a notebook cell.

## Notes

- Outlier fares are inspected but intentionally kept, since they reflect
  genuine premium/long-haul pricing rather than data errors.
- `Route` and `Additional_Info` are dropped during feature engineering —
  see Section 13 for the reasoning.
- The best-performing model (chosen by R² Score in Section 9) is what
  gets saved and served by the Flask app in Section 15–16.
