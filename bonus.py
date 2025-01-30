import pg_connector as pgc
import argparse

latest_ds = 'latest_ds.sql'
cheap_mobile = 'cheap_mobile.sql'

def execute_option(sql_file, cursor):
    with open(sql_file, 'r') as f:
            sql = f.read()#.format(region="'{}'".format(arg))
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                print(row[0])

if __name__ == "__main__":
    try:
        conn = pgc.get_connection()

        h = "Type the desired option. 'latest_ds' for the latest datasource from the two most frequent regions and 'cheap_mobile' to see which regions this datasource appears in."
        cur= conn.cursor()
        parser = argparse.ArgumentParser(description="Bonus questions")
        parser.add_argument("option", type=str, help=h)
        args = parser.parse_args()

        if args.option == 'latest_ds':
            execute_option(latest_ds, cur)
        elif args.option == 'cheap_mobile':
            execute_option(cheap_mobile, cur)

        print('Done.')
        cur.close()
        conn.close()
    except Exception as e:
        print(e)