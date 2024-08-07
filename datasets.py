 import pandas as pd
file_path = "/content/students.csv" 
df = pd.read_csv(file_path)
print("First few rows of the dataset:")
print(df.head())
print("\nLast few rows of the dataset:")
print(df.tail())
print("\nShape of the DataFrame:")
print(df.shape)
print("\nBasic information about the dataset:")
print(df.info())
print("\nSummary statistics of the dataset:")
print(df.describe())
