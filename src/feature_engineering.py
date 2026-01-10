# Feature Engineering Script
# This file contains feature engineering logic 
import pandas as pd 

df = pd.read_csv("data/taxi_cleaned.csv")

print("Cleaned Dataset saved successfully.")

print("Data loaded:", df.shape)



df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])

print("Datetime conversion done")

df["pickup_hour"] = df["tpep_pickup_datetime"].dt.hour
print("pickup_hour feature created")

print("Columns after feature:", df.columns)

df["trip_duration_min"] = (df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]).dt.total_seconds()/ 60

print("trip_duration_min feature created")

print("Columns now:", df.columns)

before = len(df)
df = df[df["trip_duration_min"] > 0]

print(f"After valid trip_duration_min (>0): {before} -> {len(df)}")

df["is_weekend"] = df["tpep_pickup_datetime"].dt.weekday >= 5
print("is_weekend feature created")

print("Columns now:", df.columns)

df["avg_speed_kmph"] = (df["trip_distance"] / df["trip_duration_min"]) * 60
print("avg_speed_kmph feature created")

print("Columns now:", df.columns)

before = len(df)
df = df[(df["avg_speed_kmph"] > 0) & (df["avg_speed_kmph"] <= 120)]
print(f"After valid avf_speed_kmph (0-120): {before} -> {len(df)}")

df.to_csv("data/taxi_features.csv", index= False)
print("Final feature engineered dataset saved: taxi_features.csv")
