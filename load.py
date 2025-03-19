import sys
import pandas as pd

if len(sys.argv) != 2:
    print("Usage: python3 load.py <dataset-path>")
    sys.exit(1)

# Load the dataset
dataset_path = sys.argv[1]
df = pd.read_csv(dataset_path)

# Display basic info about the dataset
print(f"Loaded dataset from {dataset_path}")
print(df.head())

# Save the loaded dataset as a CSV file for the next step
df.to_csv("loaded_data.csv", index=False)

# Proceed to the next step
exec(open("dpre.py").read())
