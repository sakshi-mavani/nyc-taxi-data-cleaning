# Create a smaller sample dataset from raw NYC taxi data 
# This script helps in faster testing and experimentation on large datasets 

import pandas as pd
import os

def create_sample(sample_size=100000):
    # data folder ka path
    data_folder = "data"

    # data folder me jo bhi csv mile, pehli wali le lo
    csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

    if len(csv_files) == 0:
        raise FileNotFoundError("data folder me koi CSV file nahi mili")

    raw_file = csv_files[0]   # pehli CSV
    input_path = os.path.join(data_folder, raw_file)
    output_path = os.path.join(data_folder, "taxi_sample.csv")

    print("Using file:", raw_file)

    df = pd.read_csv(input_path, nrows=sample_size)
    df.to_csv(output_path, index=False)

    print("Sample dataset created successfully")
    print("Rows, Columns:", df.shape)


if __name__ == "__main__":
    create_sample()
