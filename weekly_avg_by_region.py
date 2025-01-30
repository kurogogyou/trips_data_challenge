import pg_connector as pgc
import argparse

sql_file = 'weekly_avg_region.sql'

if __name__ == "__main__":
    try:
        conn = pgc.get_connection()

        h = "Type the region name. Available regions: Prague, Turin, Hamburg."
        cur= conn.cursor()
        parser = argparse.ArgumentParser(description="Obtain weekly average trips by region")
        parser.add_argument("region", type=str, help=h)
        args = parser.parse_args()
        with open(sql_file, 'r') as f:
            sql = f.read().format(region="'{}'".format(args.region))
            cur.execute(sql)
            result = cur.fetchall()
            for row in result:
                print(row[0])

        print('Done.')
        cur.close()
        conn.close()
    except Exception as e:
        print(e)