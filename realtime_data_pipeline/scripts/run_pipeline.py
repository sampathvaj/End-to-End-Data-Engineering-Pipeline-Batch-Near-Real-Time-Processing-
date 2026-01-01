import pandas as pd
from sqlalchemy import create_engine

# Read cleaned CSV
df = pd.read_csv(
    "data/staging/cleaned_transactions.csv",
    header=0
)


# MySQL connection (PASSWORD SET)
engine = create_engine(
    "mysql+pymysql://root:sam4477@localhost:3306/sales_db"
)

# Load data into SQL table
df.to_sql(
    "transactions_clean",
    engine,
    if_exists="append",
    index=False
)

print("✅ Data loaded into MySQL successfully")
