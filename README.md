# ✈️ PRCP-1025: Flight Fare Prediction Using Machine Learning

> **An End-to-End Data Science Capstone Project for Predicting Airline Ticket Prices Using Machine Learning Regression Algorithms**

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Application-black?logo=flask)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📌 Project Overview

Airline ticket prices are highly dynamic and fluctuate based on numerous factors such as airline, travel date, departure time, duration, number of stops, source, destination, and demand.

This project develops an intelligent **Machine Learning Regression Model** capable of accurately predicting flight ticket prices using historical flight booking data. Multiple regression algorithms are trained, evaluated, and compared to identify the most suitable model for production deployment.

The project also includes an interactive **Flask Web Application** that allows users to enter flight details and instantly receive predicted airfare through a clean black-and-white interface.

---

# 🎯 Problem Statement

Flight ticket prices are extremely unpredictable.

The same flight may cost:

* ₹4,850 today
* ₹5,920 tomorrow
* ₹4,200 next week

Such fluctuations make it difficult for travelers to determine the optimal booking time.

The objective of this project is to analyze historical flight data and build a predictive machine learning model capable of estimating future flight fares based on various flight attributes.

---

# 🎯 Project Objectives

* Perform comprehensive Exploratory Data Analysis (EDA)
* Understand the factors influencing flight fares
* Clean and preprocess the dataset
* Engineer meaningful features from date and time information
* Train multiple Machine Learning regression models
* Compare model performance using regression metrics
* Select the best-performing model
* Deploy the trained model using Flask
* Enable real-time fare prediction through a web application

---

# 📂 Repository Structure

```text
PRCP-1025-FlightFarePrediction/
│
├── PRCP-1025-FlightFarePrediction.ipynb
├── Flight_Fare.xlsx
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── flight_fare_model.pkl
├── model_columns.pkl
├── dropdown_values.pkl
│
├── README.md
└── requirements.txt
```

---

# 📊 Dataset Information

The dataset contains historical flight booking records collected from various airlines operating across India.

### Target Variable

**Price**

The machine learning model predicts the airfare based on flight specifications.

---

## Input Features

| Feature         | Description                  |
| --------------- | ---------------------------- |
| Airline         | Airline company              |
| Date_of_Journey | Journey date                 |
| Source          | Departure city               |
| Destination     | Arrival city                 |
| Route           | Travel route                 |
| Dep_Time        | Flight departure time        |
| Arrival_Time    | Flight arrival time          |
| Duration        | Total journey duration       |
| Total_Stops     | Number of stops              |
| Additional_Info | Additional services          |
| Price           | Flight ticket price (Target) |

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Flask
* OpenPyXL
* Jupyter Notebook
* VS Code

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/PRCP-1025-FlightFarePrediction.git

cd PRCP-1025-FlightFarePrediction
```

Install dependencies

```bash
pip install numpy pandas matplotlib seaborn scikit-learn flask joblib openpyxl
```

---

# ▶️ Running the Project

## Step 1

Place

```text
Flight_Fare.xlsx
```

inside the project folder.

---

## Step 2

Open

```text
PRCP-1025-FlightFarePrediction.ipynb
```

using

* Jupyter Notebook
* JupyterLab
* VS Code

---

## Step 3

Run all notebook cells sequentially.

The notebook automatically performs

* Data Cleaning
* Feature Engineering
* Model Training
* Model Evaluation
* Model Comparison
* Model Saving

No manual intervention is required.

---

# 📖 Project Workflow

```text
Problem Understanding
          │
          ▼
Dataset Collection
          │
          ▼
Data Cleaning
          │
          ▼
Exploratory Data Analysis
          │
          ▼
Feature Engineering
          │
          ▼
Data Preprocessing
          │
          ▼
Train-Test Split
          │
          ▼
Regression Model Training
          │
          ▼
Hyperparameter Tuning
          │
          ▼
Model Evaluation
          │
          ▼
Model Comparison
          │
          ▼
Best Model Selection
          │
          ▼
Model Deployment
          │
          ▼
Flask Web Application
```

---

# 📚 Notebook Contents

| Section | Description                                                   |
| ------- | ------------------------------------------------------------- |
| 1       | Problem Statement & Business Objective                        |
| 2       | Import Required Libraries                                     |
| 3       | Dataset Loading & Domain Understanding                        |
| 4       | Dataset Inspection (Shape, Types, Missing Values, Duplicates) |
| 5       | Exploratory Data Analysis (EDA)                               |
| 6       | Feature Engineering & Data Preprocessing                      |
| 7       | Regression Model Building                                     |
| 8       | Hyperparameter Tuning (GridSearchCV)                          |
| 9       | Regression Model Comparison                                   |
| 10      | Feature Importance Analysis                                   |
| 11      | Predicting Fare for New Flight Data                           |
| 12      | Business Insights                                             |
| 13      | Challenges Faced & Solutions                                  |
| 14      | Final Conclusion                                              |
| 15      | Model Serialization using Joblib                              |
| 16      | Flask Web Application                                         |
| 17      | Project References & Links                                    |

---

# 🤖 Machine Learning Models

The following regression algorithms are trained and evaluated.

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* K-Nearest Neighbors Regressor
* Support Vector Regressor (SVR)
* Gradient Boosting Regressor

---

# 📈 Model Evaluation Metrics

Performance is measured using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

The best-performing regression model is selected based on the highest **R² Score** and lowest prediction error.

---

# 🚀 Flask Web Application

The notebook automatically generates:

```text
app.py

templates/
    index.html

static/
    style.css
```

along with the trained model files:

```text
flight_fare_model.pkl

model_columns.pkl

dropdown_values.pkl
```

---

## Launch the Application

Run

```bash
python app.py
```

Open your browser

```text
http://127.0.0.1:5000
```

Enter

* Airline
* Source
* Destination
* Journey Date
* Departure Time
* Arrival Time
* Duration
* Number of Stops

Click

```text
Predict Fare
```

The application instantly predicts the estimated flight ticket price.

---

# 📊 Key Project Highlights

✅ Comprehensive Exploratory Data Analysis

✅ Advanced Feature Engineering

✅ Multiple Regression Algorithms

✅ Hyperparameter Optimization

✅ Model Performance Comparison

✅ Feature Importance Analysis

✅ Business Insights

✅ Interactive Flask Deployment

✅ Production-Ready Prediction Pipeline

---

# 💼 Business Value

This project provides value to:

### ✈️ Airlines

* Dynamic pricing support
* Revenue optimization
* Fare trend analysis

### 🧳 Travelers

* Better booking decisions
* Fare estimation before booking
* Budget planning

### 📈 Travel Platforms

* Intelligent fare recommendation
* Price forecasting
* Customer experience enhancement

---

# ⚠️ Challenges Faced

* Missing values
* Time-based feature extraction
* Encoding categorical variables
* High-cardinality features
* Feature selection
* Regression model optimization
* Preventing overfitting
* Selecting the most accurate model

---

# 🔮 Future Enhancements

* XGBoost & LightGBM implementation
* Deep Learning Regression Models
* Live Flight API integration
* Cloud deployment (AWS/Azure)
* Docker containerization
* CI/CD automation
* Interactive Power BI dashboard
* Mobile-responsive web application

---

# 👩‍💻 Author

**Sameeksha Rai**

AI & Data Science Enthusiast

* Python
* Machine Learning
* Deep Learning
* Computer Vision
* Natural Language Processing
* Generative AI

---

# ⭐ Support

If you found this project useful, please consider giving the repository a **⭐ Star**.

Your support motivates me to build and share more Machine Learning and AI projects.

---

# 📄 License

This project is intended for educational and learning purposes.

Feel free to fork, modify, and extend it for your own learning and research.
