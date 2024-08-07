import pandas as pd
import numpy as np
data = {'Age': [25, np.nan, 30, 28, 25, 35, 40, 25, 25, 100],
        'Income': ['25K', '30K', '35K', '40K', '25K', '50K', '60K', '25K', '25K', '1000K'],
        'City': ['vizag', 'chennai', 'karnataka', 'Hyderabad', 'vizag', 'chennai', 'karnataka', 'vizag', 'vizag', 'odisa']}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df['Age'].fillna(df['Age'].mean(), inplace=True)
print("\nDataFrame after handling missing values:")
print(df)
df.drop_duplicates(inplace=True)
print("\nDataFrame after removing duplicates:")
print(df)
df['Income'] = df['Income'].str.replace('K', '').astype(int)
print("\nDataFrame after converting data types:")
print(df)
df['Age'] = df['Age'].clip(lower=df['Age'].quantile(0.05), upper=df['Age'].quantile(0.95))
print("\nDataFrame after handling outliers:")
print(df)
