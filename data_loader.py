#data_loader.py
import pandas as pd
import sqlite3
from sqlalchemy import create_engine

def load_data(csv_file_path="dummy_data.csv"):
    """Loads data from a CSV file into Pandas DataFrame and SQLite database."""
    try:
        df = pd.read_csv(csv_file_path)
    except FileNotFoundError:
        print(f"Error: CSV file not found at {csv_file_path}")
        return None, None, None

    # Load into SQLite (in-memory for simplicity)
    conn = sqlite3.connect(':memory:')
    df.to_sql('employees', conn, if_exists='replace', index=False)
    engine = create_engine('sqlite:///:memory:') # For LangChain SQLDatabase
    df.to_sql('employees', engine, if_exists='replace', index=False)

    return df, engine, conn

if __name__ == "__main__":
    pandas_df, sql_engine, sql_conn = load_data()
    if pandas_df is not None:
        print("Pandas DataFrame:")
        print(pandas_df)
        print("\nData loaded into SQLite (in-memory) from dummy_data.csv.")
        sql_conn.close()
    else:
        print("Failed to load data.")