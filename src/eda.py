# Exploratory Data Analysis (EDA)
# This file contains EDA logic 
import pandas as pd 

df= pd.read_csv("data/taxi_sample.csv")
print(df)

print(df.info())
print(df.describe())

# CLEANING RULES (Based on EDA)
# 1. trip_distance > 0
# 2. fare_amount > 0
# 3. total_amount > 0
# 4. passenger_count between 1 and 6
# 5. remove extreme outliers (later using IQR)

df = pd.read_csv("data/taxi_features.csv")

print("Dataset shape:", df.shape)
print("Target columns:", "fare_amount")

print(df["fare_amount"].describe())

Q1 = df["fare_amount"].quantile(0.25)
Q3 = df["fare_amount"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

before = len(df)
df = df[(df["fare_amount"] >= lower) & (df["fare_amount"] <= upper)]

print(f"Fare outliers removed (IQR): {before} -> {len(df)}")

num_features = [
    "trip_distance",
    "trip_duration_min",
    "avg_speed_kmph",
    "pickup_hour",
    "passenger_count"
]

for col in num_features:
    print(f"\n--{col} vs fare_amount---")
    print(df.groupby(col)["fare_amount"].mean().head())

cat_features = [
    "payment_type",
    "RateCodeID",
    "is_weekend",
    "store_and_fwd_flag"
]

for col in cat_features:
    print(f"\n--- {col} vs fare_amount ---")
    print(df.groupby(col)["fare_amount"].mean().sort_values(ascending=False))
