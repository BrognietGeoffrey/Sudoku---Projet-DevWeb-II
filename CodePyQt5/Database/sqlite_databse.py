import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"sudokudb.db"

    sql_create_players_table = """CREATE TABLE IF NOT EXISTS players (
                                        player_id integer NOT NULL PRIMARY KEY,
                                        player_name text NOT NULL,
                                        password_player text NOT NULL
                                        );"""
    sql_create_classement_table = """CREATE TABLE IF NOT EXISTS classement (
                                        player_id INTEGER NOT NULL PRIMARY KEY,
                                        player_score double NOT NULL,
                                        CONSTRAINT fk_classement_player_id FOREIGN KEY (player_id) REFERENCES players (player_id)
                                        );"""
    sql_create_grille_sudoku_table = """CREATE TABLE IF NOT EXISTS grilleSudoku (
                                            player_id INTERGER NOT NULL PRIMARY KEY,
                                            player_score double NOT NULL,
                                            date_jeu date NOT NULL,
                                            image_grille BLOB NOT NULL,
                                            CONSTRAINT fk_classement_player_id_grille FOREIGN KEY (player_id)
                                            REFERENCES players (player_id),
                                            CONSTRAINT fk_classement_player_score FOREIGN KEY (player_score) REFERENCES classement (player_score)
                                        );"""

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_players_table)
        create_table(conn, sql_create_classement_table)
        create_table(conn, sql_create_grille_sudoku_table)
    else:
        print("Error ! cannot create the database connection")


if __name__ == "__main__":
    main()

