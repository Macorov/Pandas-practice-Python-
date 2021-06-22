import pandas as pd
df = pd.read_csv('pokemon_data.csv')
df["count"] = 1
print(df.groupby(["Type 1","Type 2"]).count()["count"])
#print(df)