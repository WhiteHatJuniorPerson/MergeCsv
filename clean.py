import pandas as pd
df = pd.read_csv("mergecsv.csv")
print(df.shape)
del df ["st_raderr1"]
print(df.shape)
del df ["sy_gaiamagerr2"]
print(df.shape)