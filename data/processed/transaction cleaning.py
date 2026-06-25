import pandas as pd
import os

# Define paths
file_path = 'data/raw/08_investor_transactions.csv'
output_dir = 'data/processed'

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    
    #Standardize transaction types
    df['transaction_type'] = df['transaction_type'].str.upper().str.strip()
    df = df[df['amount_inr'] > 0]
    
    # 3. Fix date formats
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    
    # Save the cleaned file
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    df.to_csv(f'{output_dir}/08_investor_transactions_clean.csv', index=False)
    print("Transactions cleaned and saved!")
else:
    print(f"Error: {file_path} not found.")