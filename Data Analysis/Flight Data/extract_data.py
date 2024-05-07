import pandas as pd
import sqlite3

def main():
    # Read the data from the sqlite database
    conn = sqlite3.connect('rocket.db')
    
    # Extract the data from the database
    df = pd.read_sql_query('SELECT * FROM ROCKET_DATA', conn)
    
    # Output the data to a csv file
    df.to_csv('rocket_data.csv', index=False)

if __name__ == '__main__':
    main()