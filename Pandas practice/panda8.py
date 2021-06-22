import pandas as pd
import re
df = pd.read_csv('pokemon_data.csv')
k = df.loc[df["Name"].str.contains("Mega")]
print(k)
k = df.loc[df["Type 1"].str.contains("Fire|Water",regex = True)]
print(k)

df.loc[df["Type 1"] == "Fire", "Type 1"]="Agun"
print(df)
df.loc[df["Type 1"] == "Agun", "Type 1"]="Fire"
print(df)
df.loc[df["Type 1"] == "Fire", "Legendary"]=True
print(df)