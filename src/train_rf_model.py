# Train a Random Forest Regressor for NYC taxi fare prediction 
# This script trains the model, evaluates performance, and saves it for reuse 

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy as np

df = pd.read_csv("data/taxi_features.csv")

y = df["fare_amount"]

X = df[
    [
    "trip_distance",
    "trip_duration_min",
    "avg_speed_kmph",
    "pickup_hour",
    "passenger_count",
    "is_weekend",
    "payment_type",
    "RateCodeID"
    ]
]

X = pd.get_dummies(X, columns = ["payment_type"], drop_first= True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 42)

rf = RandomForestRegressor(
    n_estimators=100,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

rmse= np.sqrt(mean_squared_error(y_test, y_pred))
r2= r2_score(y_test, y_pred)

print("Random Forest RMSE:", rmse)
print("Ranodm Forest R2:", r2)

feature_importance= pd.Series(rf.feature_importances_, index= X_train.columns).sort_values(ascending= False)

print("\nTop important Features:")
print(feature_importance.head(10))

import joblib

joblib.dump(rf, "data/taxi_fare_rf_model.pkl")
print("Model saved successfully")
