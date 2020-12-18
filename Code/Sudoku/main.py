from Sudoku.create_board import Sudoku


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


if __name__ == "__main__":
    while True:
        nom = ask_name()
        if nom == "exit":
            print("Bye bye!")
            break
        game_start = Sudoku()
        game_start.game()
        game_start.get_score(nom)
