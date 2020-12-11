import psycopg2
from Code.Database.config import config


def create_tables():
    commands = (
        """ CREATE TABLE players (
        player_id SERIAL NOT NULL, 
        name_id VARCHAR(50) NOT NULL, 
        surname_id  VARCHAR(50) NOT NULL, 
        pwd VARCHAR(100) NOT NULL)"""
    )

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as Error:
        print(Error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    create_tables()
