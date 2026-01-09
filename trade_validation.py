import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Number of trades to generate
NUM_TRADES = 2000

# Sample instruments
instruments = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'TSLA', 'INFY', 'TCS']

# Trade statuses
statuses = ['SUCCESS', 'FAILED', 'CANCELLED']

# Start time (7 days ago)
start_time = datetime.now() - timedelta(days=7)

data = []

for i in range(1, NUM_TRADES + 1):
    trade_id = f"T{i:06d}"
    timestamp = start_time + timedelta(minutes=random.randint(1, 10000))
    instrument = random.choice(instruments)
    price = round(random.uniform(100, 3500), 2)
    quantity = random.randint(1, 1000)
    status = random.choices(statuses, weights=[0.85, 0.10, 0.05])[0]

    data.append([
        trade_id,
        timestamp,
        instrument,
        price,
        quantity,
        status
    ])

df = pd.DataFrame(
    data,
    columns=['Trade_ID', 'Timestamp', 'Instrument', 'Price', 'Quantity', 'Trade_Status']
)

# Intentionally add data quality issues
df.loc[np.random.choice(df.index, 30), 'Price'] = None
df.loc[np.random.choice(df.index, 20), 'Quantity'] = -1
df.loc[np.random.choice(df.index, 10), 'Trade_ID'] = df['Trade_ID'].iloc[0]

# Save file
df.to_csv("data/mock_trade_data.csv", index=False)

print("Mock trade data generated successfully!")

# -----------------------------
# STEP 2: DATA VALIDATION LOGIC
# -----------------------------

# Read the generated trade data
df = pd.read_csv("data/mock_trade_data.csv")

# 1. Missing values check
missing_price = df[df['Price'].isnull()]

# 2. Duplicate Trade_ID check
duplicate_trades = df[df.duplicated(subset=['Trade_ID'], keep=False)]

# 3. Invalid quantity check (<= 0)
invalid_quantity = df[df['Quantity'] <= 0]

# 4. Invalid trade status check
valid_status = ['SUCCESS', 'FAILED', 'CANCELLED']
invalid_status = df[~df['Trade_Status'].isin(valid_status)]

# Combine all errors into one error log
error_log = pd.concat([
    missing_price.assign(Error_Type="Missing Price"),
    duplicate_trades.assign(Error_Type="Duplicate Trade_ID"),
    invalid_quantity.assign(Error_Type="Invalid Quantity"),
    invalid_status.assign(Error_Type="Invalid Trade_Status")
])

# Save error log
error_log.to_csv("data/error_log.csv", index=False)

print("Error log created successfully!")

# -----------------------------
# STEP 3: CREATE CLEAN DATA
# -----------------------------

# Remove duplicates
clean_df = df.drop_duplicates(subset=['Trade_ID'])

# Remove invalid prices and quantities
clean_df = clean_df[(clean_df['Price'].notnull()) & (clean_df['Price'] > 0)]
clean_df = clean_df[clean_df['Quantity'] > 0]

# Keep only valid trade statuses
clean_df = clean_df[clean_df['Trade_Status'].isin(valid_status)]

# Save clean data
clean_df.to_csv("data/clean_trades.csv", index=False)

print("Clean trade data created successfully!")

# -----------------------------
# STEP 4: ACCURACY METRICS
# -----------------------------

total_records = len(df)
clean_records = len(clean_df)
error_records = len(error_log)

accuracy_percent = round((clean_records / total_records) * 100, 2)

metrics_df = pd.DataFrame({
    "Metric": [
        "Total Trades",
        "Clean Trades",
        "Error Records",
        "Data Accuracy (%)"
    ],
    "Value": [
        total_records,
        clean_records,
        error_records,
        accuracy_percent
    ]
})

# Save metrics
metrics_df.to_csv("data/metrics_summary.csv", index=False)

print("Metrics summary created successfully!")

