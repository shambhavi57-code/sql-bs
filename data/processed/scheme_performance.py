import pandas as pd
import os
file_path = 'data/raw/07_scheme_performance.csv' 
output_dir = 'data/processed'

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    df['expense_ratio_pct'] = pd.to_numeric(df['expense_ratio_pct'], errors='coerce')
    df = df[(df['expense_ratio_pct'] >= 0.1) & (df['expense_ratio_pct'] <= 2.5)]
    df_long = df.melt(
        id_vars=['amfi_code', 'scheme_name', 'fund_house', 'category', 'plan'], 
        value_vars=['return_1yr_pct', 'return_3yr_pct', 'return_5yr_pct'], 
        var_name='period', 
        value_name='return_pct'
    )
    df_long['anomaly_returns'] = (df_long['return_pct'] > 1.0) | (df_long['return_pct'] < -0.5)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    df_long.to_csv(f'{output_dir}/scheme_performance_clean.csv', index=False)
    
    print("--- Pipeline Summary ---")
    print(f"Performance data transformed and filtered.")
    print(f"Rows after filtering: {len(df_long)}")
    print(f"Anomalies detected: {df_long['anomaly_returns'].sum()}")
    print(f"File saved to: {output_dir}/scheme_performance_clean.csv")