import pandas as pd
df = pd.read_csv('pokemon_data.csv')
df["Total"]= df["Attack"] + df["Defense"]
print(df)
df = df.drop(columns=["Total"])
print(df)
df["Total"] = df.iloc[:,4,9].sum(axis = 1)