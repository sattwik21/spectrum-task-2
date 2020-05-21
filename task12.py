import pandas as satt
diamonds = satt.read_csv('diamonds.csv')
print(diamonds.shape)
print("\nSample 75% of diamonds DataFrame's rows without replacement:")
first = diamonds.sample(frac=0.75)
print(first)
print("\nRemaining 25%of the rows:")
var= diamonds.loc[~diamonds.index.isin(first.index),:]
var.to_csv('file.csv')
new = satt.read_csv('file.csv')
print(new)