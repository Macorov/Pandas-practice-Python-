import pandas as pd
df = pd.read_csv('pokemon_data.csv')
df["Total"] = df.iloc[:,4:10].sum(axis = 1)
print(df)
df = df.drop(columns=["Total"])
print(df)
df["Total"] = df.iloc[:,4:10].sum(axis = 1)
