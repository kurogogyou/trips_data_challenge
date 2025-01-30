import pandas as pd
import random
import datetime
import argparse

def generate_trips(num_trips, num_files, output_prefix):
    # Define regions and bounding boxes
    regions = {
        "Hamburg": {"min_x": 9.5, "max_x": 10.5, "min_y": 53.5, "max_y": 54.5},
        "Turin": {"min_x": 7.5, "max_x": 8.0, "min_y": 44.5, "max_y": 45.5},
        "Prague": {"min_x": 14.2, "max_x": 15.0, "min_y": 50.0, "max_y": 51.0}
    }

    # Define date range
    start_date = datetime.datetime(2018, 5, 1)
    end_date = datetime.datetime(2020, 1, 23)

    # Define datasources
    datasources = ["cheap_mobile", "baba_car", "funny_car", "bad_diesel_vehicles", "pt_search_app"]

    # Function to generate a random timestamp
    def random_datetime():
        random_date = start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))
        random_time = datetime.timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
        return (random_date + random_time).strftime('%Y-%m-%d %H:%M:%S')

    # Function to generate a random point within a bounding box
    def random_point(region):
        bbox = regions[region]
        return f"POINT({random.uniform(bbox['min_x'], bbox['max_x'])} {random.uniform(bbox['min_y'], bbox['max_y'])})"

    # Determine number of rows per file
    rows_per_file = num_trips // num_files
    remaining_rows = num_trips % num_files

    for i in range(num_files):
        file_name = f"{output_prefix}_{i+1}.csv"
        num_rows = rows_per_file + (1 if i < remaining_rows else 0)  # Distribute extra rows evenly
        trips = []
        
        for _ in range(num_rows):
            region = random.choice(list(regions.keys()))
            origin = random_point(region)
            destination = random_point(region)
            datetime_str = random_datetime()
            datasource = random.choice(datasources)
            trips.append([region, origin, destination, datetime_str, datasource])

        df = pd.DataFrame(trips, columns=["region", "origin_coord", "destination_coord", "datetime", "datasource"])
        df.to_csv(file_name, index=False)
        print(f"Generated {file_name} with {num_rows} rows.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate multiple CSV files with random trip data.")
    parser.add_argument("num_trips", type=int, help="Total number of trips to generate.")
    parser.add_argument("num_files", type=int, help="Number of output files.")
    parser.add_argument("output_prefix", type=str, help="Prefix for output CSV files.")
    args = parser.parse_args()
    
    generate_trips(args.num_trips, args.num_files, args.output_prefix)