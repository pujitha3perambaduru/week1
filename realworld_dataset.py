 import pandas as pd
from sklearn import datasets
iris = datasets.load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target

print("Iris Dataset:")
print(iris_df.head())

print("\nIris Dataset Statistics:")
print(iris_df.describe())

california_housing = datasets.fetch_california_housing()
california_df = pd.DataFrame(data=california_housing.data, columns=california_housing.feature_names)
california_df['target'] = california_housing.target

print("\nCalifornia Housing Dataset:")
print(california_df.head())

print("\nCalifornia Housing Dataset Statistics:")
print(california_df.describe())
