import pandas as pd

df = pd.read_csv("result2.csv")

df = df[df["Distance"].notna()]
df = df[df["Mass"].notna()]
df = df[df["Radius"].notna()]
#print(df)

df["Radius"] = df["Radius"]*0.102763

df["Mass"] = df["Mass"].map(lambda x: float(x))
print(df.dtypes)

df["Mass"] = df["Mass"]*0.000954588
print(df)

df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.to_csv("result2.csv")



