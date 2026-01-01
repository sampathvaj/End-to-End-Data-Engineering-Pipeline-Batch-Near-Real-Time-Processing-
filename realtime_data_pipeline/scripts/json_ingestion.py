import json
import pandas as pd
from pathlib import Path

# --------------------
# Paths
# --------------------
JSON_PATH = "data/json/transaction.json"
CSV_PATH = "data/staging/cleaned_transactions.csv"

# --------------------
# Read JSON (LIST of records)
# --------------------
with open(JSON_PATH, "r") as f:
    data = json.load(f)

# ✅ CRITICAL FIX: data is a LIST
df = pd.DataFrame(data)

# --------------------
# Validate columns (debug safety)
# --------------------
print("Columns:", df.columns.tolist())
print("Records loaded:", len(df))

# --------------------
# Cleaning
# --------------------
df.dropna(inplace=True)

df["transaction_time"] = pd.to_datetime(df["transaction_time"])
df["amount"] = df["amount"].astype(float)

df = df[df["amount"] > 0]

# --------------------
# Transformations
# --------------------
df["date"] = df["transaction_time"].dt.date
df["hour"] = df["transaction_time"].dt.hour

# --------------------
# Ensure staging folder exists
# --------------------
Path("data/staging").mkdir(parents=True, exist_ok=True)

# --------------------
# Append to CSV
# --------------------
df.to_csv(
    CSV_PATH,
    mode="a",
    header=not Path(CSV_PATH).exists(),
    index=False
)

print(f"✅ {len(df)} records appended successfully")
