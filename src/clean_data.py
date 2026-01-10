# NYC Taxi Data Cleaning Script
# This file contains data cleaning logic
import pandas as pd 
df = pd.read_csv("data/taxi_sample.csv")

print("Initial shape:", df.shape)

print("Initial rows:", len(df))

# remove invalid trip_distance
before = len(df)
df = df[df["trip_distance"]>0]
print(f"After trip_distance > 0 : {before}  -> {len(df)}")

# remove invalid fare_amount
before = len(df)
df = df[df["fare_amount"]>0]
print(f"After fare_amount > 0 : {before}  -> {len(df)}")

# remove invalid total_amount
before = len(df)
df = df[df["total_amount"]>0]
print(f"After total_amount > 0 : {before}  -> {len(df)}")

# valid passenger count
before = len(df)
df = df[df["passenger_count"].between(1,6)]
print(f"After passenger_count 1-6:{before}  -> {len(df)}")

df.to_csv("data/taxi_cleaned.csv",  index= False)
print("Cleaned dataset saved successfully")
