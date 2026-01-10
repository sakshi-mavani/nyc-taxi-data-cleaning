# Prepare final feature set and target variable for model training
# Select relevent features from engineered taxi dataset

import pandas as pd 

df = pd.read_csv("data/taxi_features.csv")

print("Data loaded:", df.shape)

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
