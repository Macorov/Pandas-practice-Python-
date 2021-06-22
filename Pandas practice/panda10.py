import pandas as pd
df = pd.read_csv('pokemon_data.csv')
a= df.groupby(["Type 1"]).mean()
print(a)
a= df.groupby(["Type 1"]).mean().sort_values("Defense", ascending=False)
print(a)