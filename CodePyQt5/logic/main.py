from CodePyQt5.logic.create_board import *
import sqlite3


def ask_name():
    """
    Function that ask the player for a valid name.

    PRE: -
    POST:
        returns a name, a string that contains the player's chosen name.
    """
    name = (input("Type your name or 'exit' to quit the game: "))
    if not name.isalpha() or name == "":
        print("You typed a number or nothing, please retry.")
        return ask_name()
    return name


def send_to_db(player_id, name, score):
    conn = sqlite3.connect(r'../../CodePyQt5/Database/sudokudb.db')  # Connection to database
    cursor = conn.cursor()  # Connection between the database and the futur query selection
    cursor.execute("""CREATE TABLE IF NOT EXISTS classement (
                                                player_id integer NOT NULL PRIMARY KEY, 
                                                player_score double NOT NULL
                                                player_name text NOT NULL,
                                                )""")
    cursor.execute("""INSERT INTO classement(player_id, password_score, player_name)
                                        VALUES(?,?, ?)""", (player_id, name, score))
    conn.commit()  # Commit to database
    cursor.close()  # end query
    conn.close()  # Close connection to database


if __name__ == "__main__":
    while True:
        nom = ask_name()
        if nom == "exit":
            print("Bye bye!")
            break
        game_start = Sudoku()
        game_start.game()
        game_start.get_score(nom)
