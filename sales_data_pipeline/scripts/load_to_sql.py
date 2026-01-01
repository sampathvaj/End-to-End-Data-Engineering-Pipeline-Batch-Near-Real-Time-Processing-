import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

# ===============================
# Project paths
# ===============================
BASE_DIR = Path(__file__).resolve().parent.parent
STAGING_PATH = BASE_DIR / "data" / "staging" / "sales_transactions_cleaned.csv"

# ===============================
# MySQL connection
# ===============================
engine = create_engine(
    "mysql+pymysql://root:sam4477@localhost/sales_db"
)

# ===============================
# Load cleaned data
# ===============================
df = pd.read_csv(STAGING_PATH)

df.to_sql(
    name="sales_clean",
    con=engine,
    if_exists="replace",   # replace only this table
    index=False
)

print("✅ Data successfully loaded into MySQL (sales_clean)")
print(f"Rows inserted: {len(df)}")
