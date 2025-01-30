import glob
from tqdm import tqdm
import argparse
import pg_connector as pgc

# Source file locations
data_folder = r'source_data/'
source_files = glob.glob(f"{data_folder}/*.csv") 

# Query files
initialize_query = 'pg_init.sql'
transform_query = 'pg_transform_trips.sql'

def total_file_rows(filename):
    with open(filename, 'r') as f:
        total_rows = sum(1 for line in f) - 1
        return total_rows

def initialize_db(cursor):
    with open(initialize_query, 'r') as i:
        print('Initializing...')
        cursor.execute(i.read())
        print('Initialization done.')

def ingest_trip_data(cursor):
    counter = 1
    total_files = len(source_files)
    for filename in source_files:
        print('Reading file {} of {}'.format(counter,total_files))
        print(filename)
        with open(filename, 'r') as f:
            next(f) # Skip header
            total_rows = total_file_rows(filename)
            with tqdm(total=total_rows, desc="Ingesting data", unit='rows') as pbar:
                cursor.copy_expert('COPY raw_trips(region,origin_coord,destination_coord,datetime,datasource) from stdin with CSV', f)
                pbar.update(total_rows)
            with open(transform_query, 'r') as q:
                print('Transforming...')
                cursor.execute(q.read()) 
        cursor.execute('truncate raw_trips;')
        counter += 1

if __name__ == "__main__":
    try:
        conn = pgc.get_connection()

        h = "Type 'init' for initializing and 'ingest' for data ingestion."
        cur= conn.cursor()
        parser = argparse.ArgumentParser(description="Initialize DB or ingest trip data in source folder")
        parser.add_argument("option", type=str, help=h)
        args = parser.parse_args()
        if args.option == 'init':
            initialize_db(cur)
        elif args.option == 'ingest':
            ingest_trip_data(cur)
        else:
            print(h)

        print('Done.')
        cur.close()
        conn.close()
    except Exception as e:
        print(e)