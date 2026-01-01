import pandas as pd
from pathlib import Path
import numpy as np

# ===============================
# Project paths
# ===============================
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_PATH = BASE_DIR / "data" / "raw" / "sales_transactions_raw.csv"
STAGING_PATH = BASE_DIR / "data" / "staging" / "sales_transactions_cleaned.csv"

# ===============================
# Step 1: Read raw data
# ===============================
df = pd.read_csv(RAW_PATH)

# ===============================
# Step 2: Clean base data
# ===============================
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# ===============================
# Step 3: EXPAND TO 5000 RECORDS
# ===============================
TARGET_ROWS = 5000

df_5000 = df.sample(
    n=TARGET_ROWS,
    replace=True,          # 🔑 THIS creates more rows
    random_state=42
).reset_index(drop=True)

# ===============================
# Step 4: Transform data
# ===============================
df_5000["order_date"] = pd.to_datetime(df_5000["order_date"])
df_5000["year"] = df_5000["order_date"].dt.year
df_5000["month"] = df_5000["order_date"].dt.month

# Optional: make order_id unique
df_5000["order_id"] = range(1, len(df_5000) + 1)

# ===============================
# Step 5: Save cleaned data
# ===============================
df_5000.to_csv(STAGING_PATH, index=False)

print("✅ 5000 records generated and saved successfully")
print("Final record count:", len(df_5000))
