import pandas as pd
df = pd.read_csv('pokemon_data.csv')
df.loc[df["HP"]>60,["Generation","Legendary"]] = ["Alpha","Super"]
print(df)