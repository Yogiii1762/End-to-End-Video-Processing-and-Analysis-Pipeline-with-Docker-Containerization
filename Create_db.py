import pandas as pd
import sqlite3
import os

def store_results_in_db(csv_file):
    
    db_file = "detection_results.db"
    
    
    if not os.path.exists(csv_file):
        print(f"Error: CSV file not found: {csv_file}")
        return None

    try:
        df = pd.read_csv(csv_file)
        df['duration_in_minutes'] = df['Timestamp'].apply(convert_to_minutes)

        conn = sqlite3.connect(db_file)
        df.to_sql('detection_results', conn, if_exists='replace', index=False)

    finally:
        conn.close()

    print(f"Data stored in {db_file}")
    return db_file

def convert_to_minutes(time_str):
    try:
       
        time_parts = time_str.split(':')
        
    
        hours = float(time_parts[0])
        minutes = float(time_parts[1])
        seconds = float(time_parts[2])

        total_minutes = hours * 60 + minutes + seconds / 60
        
        return total_minutes

    except Exception as e:
        print(f"Error converting time {time_str}: {e}")
        return 0

if __name__ == "__main__":
    csv_file = "Detection_Results.csv"
    store_results_in_db(csv_file)
