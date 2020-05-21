import pandas as pd
diamonds = pd.read_csv('diamonds.csv')
print("\nCount,minimum,maximum price for each cut of diamonds DataFrame:")
print(diamonds.groupby('cut').price.agg(['count','min','max']))