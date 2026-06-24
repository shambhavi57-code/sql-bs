import pandas as pd
import os
from sqlalchemy import create_engine
engine = create_engine('sqlite:///bluestock_mf.db')
data_map = {
    'fact_nav': 'data/processed/02_nav_history_clean.csv',
    'fact_transactions': 'data/processed/08_investor_transactions_clean.csv',
    'fact_performance': 'data/processed/scheme_performance_clean.csv'
}
for table, path in data_map.items():
    if os.path.exists(path):
        df = pd.read_csv(path)
        # Usi
        df.to_sql(table, engine, if_exists='append', index=False)
        print(f"Loaded {path} into {table}")
    else:
        print(f"Skipping {path}: File not found.")