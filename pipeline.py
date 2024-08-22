#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')
    parser.add_argument('--user', help='user name for postgres', required=True)
    parser.add_argument('--password', help='password for postgres', required=True)
    parser.add_argument('--host', help='host for postgres', required=True)
    parser.add_argument('--port', help='port for postgres', required=True)
    parser.add_argument('--db', help='database name for postgres', required=True)
    parser.add_argument('--table_name', help='name of the table where we will write the results to', required=True)
    return parser.parse_args()

def make_connection(conn: str):
    return create_engine(conn).connect()

def read_data_from_csv(file_path: str):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading data from CSV: {e}")
        return None

def manipulate_data(df: pd.DataFrame):
    df['date'] = pd.to_datetime(df['date'])
    df['arrest'] = df['arrest'].astype(bool)
    df['domestic'] = df['domestic'].astype(bool)
    return df

def push_to_db(df: pd.DataFrame, engine, table_name: str):
    chunk_size = 10000
    num_chunks = len(df) // chunk_size + 1

    for i in range(num_chunks):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size
        chunk = df.iloc[start_idx:end_idx]

        try:
            chunk.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
            chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False)
            print(f"Data successfully pushed to the database for chunk {i + 1}/{num_chunks}.")
        except Exception as e:
            print(f"Error pushing data to the database: {e}")

def main():
    args = parse_arguments()
    connection_string = f'postgresql://{args.user}:{args.password}@{args.host}:{args.port}/{args.db}'
    table_name = args.table_name

    # Execution
    engine = make_connection(connection_string)
    if engine:
        data_path = 'FBI_data/extracted_chicago_crime_data.csv'
        data_frame = read_data_from_csv(data_path)
        if data_frame is not None:
            manipulated_data = manipulate_data(data_frame)
            push_to_db(manipulated_data, engine, table_name)
            print("Data pushed successfully")
        else:
            print("Failed to read data from CSV.")
    else:
        print("Failed to establish a database connection.")

if __name__ == "__main__":
    main()
