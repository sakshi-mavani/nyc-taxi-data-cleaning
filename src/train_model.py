# Train a linear Regression model to predict NYC taxi fare
# This script splits data, trains the model, and evaluates performance 

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
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

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("RMSE:", rmse)
print("R2 Score:", r2)
