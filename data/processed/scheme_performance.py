import pandas as pd
import os

file_path = 'data/raw/07_scheme_performance.csv' 
output_dir = 'data/processed'

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
   
    df_long = df.melt(
        id_vars=['amfi_code', 'scheme_name', 'fund_house', 'category', 'plan'], 
        value_vars=['return_1yr_pct', 'return_3yr_pct', 'return_5yr_pct'], 
        var_name='period', 
        value_name='return_pct'
    )
    df_long['anomaly_expense_ratio'] = df['expense_ratio_pct'] > 0.05
    df_long['anomaly_returns'] = (df_long['return_pct'] > 1.0) | (df_long['return_pct'] < -0.5)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    df_long.to_csv(f'{output_dir}/scheme_performance_clean.csv', index=False)
    print("Performance data transformed, validated, and saved!")
else:
    print(f"Error: {file_path} not found.")