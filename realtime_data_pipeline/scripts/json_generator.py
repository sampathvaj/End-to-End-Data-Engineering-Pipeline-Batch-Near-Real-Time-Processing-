import json
import random
from datetime import datetime
from pathlib import Path

RECORD_COUNT = 10000
records = []

for _ in range(RECORD_COUNT):
    records.append({
        "transaction_id": random.randint(100000, 999999),
        "transaction_time": datetime.now().isoformat(),
        "customer_id": random.randint(1, 5000),
        "region": random.choice(["North", "South", "East", "West"]),
        "amount": round(random.uniform(100, 5000), 2)
    })

Path("data/json").mkdir(parents=True, exist_ok=True)

with open("data/json/transaction.json", "w") as f:
    json.dump(records, f)

print(f"✅ {RECORD_COUNT} records generated")
