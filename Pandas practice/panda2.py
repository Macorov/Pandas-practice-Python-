import pandas as pd
df = pd.read_csv('pokemon_data.csv')
print(df.iloc[0:3])
print(df.iloc[6,1])
print(df.iloc[0,1])
print(df.iloc[:,1])