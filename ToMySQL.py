import os
import pandas as pd
from sqlalchemy import create_engine

# Set path to the folder containing the CSV files
folder_path = '/Users/davidkang/Desktop/HfT Stuttgart/Business Intelligence/Pre Exam/BI - Pre Exam'

# Connect to MySQL
engine = create_engine('mysql+pymysql://root:hftbi2024winter@localhost:3306/BIPVL_DB')

# Loop through each file in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        
        # Load CSV into pandas DataFrame
        df = pd.read_csv(file_path)
        
        # Shorten column names to comply with MySQL's 64 character limit
        df.columns = [col[:64] if len(col) > 64 else col for col in df.columns]
        
        # Define table name based on file name (optional: can customize table naming strategy)
        table_name = file_name.replace('.csv', '')
        
        # Store the data in MySQL
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Imported {file_name} into the database table {table_name}")
