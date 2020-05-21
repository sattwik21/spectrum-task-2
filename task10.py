import pandas as satt
diamonds = satt.read_csv('diamonds.csv')
print("Number of rows and columns:")
print(diamonds.shape)
print("After dropping those rows whose where values are missing:")
print(diamonds.dropna(how='any').shape)