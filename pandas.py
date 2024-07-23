import pandas as pd
import numpy as np
series = pd.Series([1, 2, 3, 4, 5])
print("Series:\n", series)

data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

print("\nFirst 5 rows of DataFrame:\n", df.head())
print("\nLast 5 rows of DataFrame:\n", df.tail())

print("\nDataFrame Info:")
df.info()
print("\nDataFrame Description:\n", df.describe())

grouped_df = df.groupby('A').sum()
print("\nGrouped DataFrame by column 'A' and summed:\n", grouped_df)

data2 = {
    'A': [1, 2, 3, 6, 7],
    'D': [1000, 2000, 3000, 6000, 7000]
}
df2 = pd.DataFrame(data2)
merged_df = pd.merge(df, df2, on='A', how='inner')
print("\nMerged DataFrame:\n", merged_df)

df_dropped = df.drop(columns=['B'])
print("\nDataFrame after dropping column 'B':\n", df_dropped)

data_with_nan = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [10, 20, 30, np.nan, 50]
}
df_nan = pd.DataFrame(data_with_nan)
print("\nDataFrame with NaN values:\n", df_nan)

filled_df = df_nan.fillna(0)
print("\nDataFrame after filling NaN values with 0:\n", filled_df)

df_nan['A'] = df_nan['A'].apply(lambda x: 0 if pd.isnull(x) else x)
print("\nDataFrame after applying function to fill NaN in column 'A':\n", df_nan)

print("\nChecking for NaN values:\n", df_nan.isnull())
print("\nChecking for non-NaN values:\n", df_nan.notnull())

sorted_values_df = df.sort_values(by='B')
print("\nDataFrame sorted by column 'B':\n", sorted_values_df)

sorted_index_df = df.sort_index()
print("\nDataFrame sorted by index:\n", sorted_index_df)
