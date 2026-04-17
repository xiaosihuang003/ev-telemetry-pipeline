import pandas as pd

df = pd.read_csv("data/ChargingRecords.csv")

# Convert datetime columns to proper datetime type
df["StartDatetime"] = pd.to_datetime(df["StartDatetime"])
df["EndDatetime"] = pd.to_datetime(df["EndDatetime"])

# Calculate actual duration in minutes from datetime columns
df["calculated_duration"] = (df["EndDatetime"] - df["StartDatetime"]).dt.total_seconds() / 60

# Compare with existing Duration column
print("First 5 rows - Duration vs calculated_duration:")
print(df[["StartDatetime", "EndDatetime", "Duration", "calculated_duration"]].head())# import pandas as pd

# df = pd.read_csv("data/ChargingRecords.csv")

# # Convert datetime columns to proper datetime type
# df["StartDatetime"] = pd.to_datetime(df["StartDatetime"])
# df["EndDatetime"] = pd.to_datetime(df["EndDatetime"])

# print("Data types after conversion:")
# print(df.dtypes)

# print("\nNull values per column:")
# print(df.isnull().sum())