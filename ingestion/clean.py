import pandas as pd

df = pd.read_csv("data/ChargingRecords.csv")

# Convert datetime columns to proper datetime type
df["StartDatetime"] = pd.to_datetime(df["StartDatetime"])
df["EndDatetime"] = pd.to_datetime(df["EndDatetime"])

print("Data types after conversion:")
print(df.dtypes)

print("\nNull values per column:")
print(df.isnull().sum())