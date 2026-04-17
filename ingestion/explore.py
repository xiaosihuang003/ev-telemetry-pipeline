import pandas as pd

df = pd.read_csv("data/ChargingRecords.csv")

print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 3 rows:")
print(df.head(3))
print("\nData types:")
print(df.dtypes)