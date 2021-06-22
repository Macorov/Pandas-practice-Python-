import pandas as pd
df = pd.read_csv('pokemon_data.csv')
k = df.loc[(df["Type 1"]=="Grass") & (df["Type 2"]=="Poison")]
k = k.reset_index()
print(k)
k.to_csv("new.csv")