# nyc-taxi-data-cleaning
NYC taxi data cleaning, feature engineering and fare prediction project 
# NYC Taxi Fare Prediction

This is a small end-to-end data science project that I built while learning data science.
I used the NYC Yellow Taxi dataset to understand how a real-world dataset is cleaned,
analyzed and used to train machine learning models.

The main goal of this project is to predict the taxi fare amount using trip details
like distance, duration, pickup time and passenger count.

I did this project mainly for learning and practice, and to understand how industry-level
projects are structured.

---

## Project Structure

NYC Taxi Data Cleaning/

data/
- taxi_sample.csv (sample data for testing)
- taxi_cleaned.csv (after cleaning)
- taxi_features.csv (after feature engineering)

src/
- clean_data.py (cleaning the raw data)
- eda.py (basic analysis and understanding data)
- feature_engineering.py (creating new features)
- model_ready.py (preparing data for ML)
- train_model.py (linear regression model)
- train_rf_model.py (random forest model)

README.md

---

## Problem Statement

Given taxi trip details, predict the fare amount.
This is a regression problem and very common in ride-hailing type companies.

---

## Data Cleaning

The raw data had many invalid values.
So I cleaned the data by:
- removing trips with zero or negative distance
- removing trips with invalid fare values
- keeping passenger count between 1 and 6
- removing extreme outliers using IQR

Cleaning helped improve data quality and model performance.

---

## Exploratory Data Analysis (EDA)

I performed EDA to understand:
- how fare amount is distributed
- how distance and duration affect fare
- which features are important for prediction

EDA helped me decide which features to keep for modeling.

---

## Feature Engineering

I created a few useful features:
- trip duration in minutes
- pickup hour from datetime
- weekend flag
- average speed of the trip

These features helped the model understand the data better.

---

## Models Used

### Linear Regression
I first trained a Linear Regression model as a baseline.
It performed reasonably well and helped me understand the data.

RMSE was around 2.6 and R² score was about 0.93.

---

### Random Forest Regression
Then I trained a Random Forest model.
This model performed much better than Linear Regression.

RMSE was around 1.7 and R² score was close to 0.96.

---

## What I Learned

- how real-world data is cleaned
- why feature engineering is important
- how to build a baseline model
- how to compare different models
- how an industry-style data science workflow looks

---

## Conclusion

This project helped me gain confidence in working with real datasets.
I plan to improve this project further by trying advanced models and deployment.

Thanks for checking out my project...Sakshi
