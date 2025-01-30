import pg_connector as pgc
import argparse

sql_file = 'weekly_avg_bound_box.sql'

if __name__ == "__main__":
    try:
        conn = pgc.get_connection()

        #h = "Type the region name. Available regions: Prague, Turin, Hamburg."
        cur= conn.cursor()
        parser = argparse.ArgumentParser(description="Obtain weekly average trips by bounding box.")
        parser.add_argument("origin_min_x", type=str, help='Origin minimum latitude. Input as decimal.')
        parser.add_argument("origin_max_x", type=str, help='Origin maximum latitude. Input as decimal.')
        parser.add_argument("origin_min_y", type=str, help='Origin minimum longitude. Input as decimal.')
        parser.add_argument("origin_max_y", type=str, help='Origin maximum longitude. Input as decimal.')
        parser.add_argument("dest_min_x", type=str, help='Destination minimum latitude. Input as decimal.')
        parser.add_argument("dest_max_x", type=str, help='Destination maximum latitude. Input as decimal.')
        parser.add_argument("dest_min_y", type=str, help='Destination minimum longitude. Input as decimal.')
        parser.add_argument("dest_max_y", type=str, help='Destination maximum longitude. Input as decimal.')
        args = parser.parse_args()
        with open(sql_file, 'r') as f:
            sql = f.read().format(
                origin_min_x="{}".format(args.origin_min_x),
                origin_max_x="{}".format(args.origin_max_x),
                origin_min_y="{}".format(args.origin_min_y),
                origin_max_y="{}".format(args.origin_max_y),
                dest_min_x="{}".format(args.dest_min_x),
                dest_max_x="{}".format(args.dest_max_x),
                dest_min_y="{}".format(args.dest_min_y),
                dest_max_y="{}".format(args.dest_max_y),
                )
            cur.execute(sql)
            result = cur.fetchall()
            for row in result:
                print(row[0])

        print('Done.')
        cur.close()
        conn.close()
    except Exception as e:
        print(e)