import pandas as satt
diamonds = satt.read_csv('diamonds.csv')
data = input("Enter a series from data frame")
print(diamonds[data])