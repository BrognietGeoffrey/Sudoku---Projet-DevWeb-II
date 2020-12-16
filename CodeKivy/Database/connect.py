import psycopg2
from CodeKivy.Database.config import config


def connect():
    conn = None
    try:
        params = config()
        print('Connecting to the PostGreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print("PostGreSQL database version")
        cur.execute('Select Version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as Error:
        print(Error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed')


if __name__ == "__main__":
    connect()

