import pandas as pd
import os
file_path = 'data/raw/02_nav_history.csv'
output_dir = 'data/processed'
if os.path.exists(file_path):
    print(f"Success! Found file at: {file_path}")
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by=['amfi_code', 'date'])
    df['nav'] = df.groupby('amfi_code')['nav'].ffill()
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    df.to_csv(f'{output_dir}/02_nav_history_clean.csv', index=False)
    print("Data processed and saved successfully!")
else:
    print(f"Error: Could not find the file at {file_path}")
file_path = 'data/raw/02_nav_history.csv'
if os.path.exists(file_path):
    print(f"Success! Found file at: {file_path}")
    
    # Load the data
    df = pd.read_csv(file_path)
    
    # Clean the data
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by=['amfi_code', 'date'])
    df['nav'] = df.groupby('amfi_code')['nav'].ffill()
    
    # Save the file
    df.to_csv('data/processed/02_nav_history_clean.csv', index=False)
    print("Data processed and saved to data/processed/02_nav_history_clean.csv")
else:
    print(f"Error: Cannot find the file at {os.path.abspath(file_path)}")