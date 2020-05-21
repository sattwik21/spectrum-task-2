import pandas as pd
diamonds = pd.read_csv('diamonds.csv')
print("Original Dataframe:")
print(diamonds.shape)
print("\nDuplicate rows of diamonds DataFrame:")
print(diamonds.duplicated().sum())