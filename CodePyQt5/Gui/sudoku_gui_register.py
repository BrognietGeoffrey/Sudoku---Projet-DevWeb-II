from CodePyQt5.Gui.sudokuguilogin import *
import sqlite3
from PyQt5 import QtCore, QtWidgets, QtGui


class GuiRegister(object):
    def window_open(self):
        self.window = QtWidgets.QMainWindow()
        self.change = GuiLogin()
        self.change.login_window(self.window)
        self.window.show()

    def register_window(self, NewPlayer):
        NewPlayer.setObjectName("NewPlayer")
        NewPlayer.resize(600, 400)

        self.tb = QtWidgets.QTextBrowser(NewPlayer)
        self.tb.setGeometry(QtCore.QRect(150, 10, 361, 61))
        self.tb.setText("REGISTER")
        self.tb.setObjectName("text_browser")

        self.glw = QtWidgets.QWidget(NewPlayer)
        self.glw.setGeometry(QtCore.QRect(100, 90, 431, 261))
        self.glw.setObjectName("grid_layout_widget")

        self.gl = QtWidgets.QGridLayout(self.glw)
        self.gl.setContentsMargins(0, 0, 0, 0)
        self.gl.setObjectName("grid_layout")

        self.p_username = QtWidgets.QLabel(self.glw)
        self.p_username.setObjectName("p_username")
        self.gl.addWidget(self.p_username, 0, 0, 1, 1)
        self.p_username.setText("Username : ")

        self.p_password = QtWidgets.QLabel(self.glw)
        self.p_password.setObjectName("p_password")
        self.gl.addWidget(self.p_password, 1, 0, 1, 1)
        self.p_password.setText("Password : ")

        self.tp = QtWidgets.QLineEdit(self.glw)
        self.tp.setObjectName("text_password")

        self.gl.addWidget(self.tp, 1, 1, 1, 1)
        self.tu = QtWidgets.QLineEdit(self.glw)
        self.tu.setObjectName("text_username")
        self.gl.addWidget(self.tu, 0, 1, 1, 1)

        self.button_exit = QtWidgets.QPushButton(self.glw)
        self.button_exit.setStyleSheet("background-color: rgb(15, 15, 15; color:\'white\'")
        self.button_exit.setObjectName("button_login")
        self.button_exit.setText("Return to sign in page")

        self.gl.addWidget(self.button_exit, 3, 1, 1, 1)

        self.button_register = QtWidgets.QPushButton(self.glw)
        self.button_register.setStyleSheet("background-color: rgb(20, 20, 20")
        self.button_register.setObjectName("button_register")
        self.button_register.setText("REGISTER")

        self.gl.addWidget(self.button_register, 2, 1, 1, 1)

        self.button_register.clicked.connect(self.database)
        self.button_exit.clicked.connect(self.button_exit_action)

    def button_exit_action(self):
        self.window_open()

    def popup_register_window(self, text):
        popup_message = QtWidgets.QMessageBox()
        popup_message.setIcon(QtWidgets.QMessageBox.Critical)
        popup_message.setText("{}".format(text))
        popup_message.setInformativeText('{}'.format(text))
        popup_message.setWindowTitle("{}".format(text))

        popup_message.exec_()

    def database(self):
        try:
            txt_username = self.tu.text()
            txt_password = self.tp.text()

            conn = sqlite3.connect(
                r'../../CodePyQt5/Database/sudokudb.db')
            print(sqlite3.version)
            cursor = conn.cursor()

            cursor.execute("""CREATE TABLE IF NOT EXISTS players (
                                        player_id integer NOT NULL PRIMARY KEY, 
                                        player_name text NOT NULL, 
                                        password_player text NOT NULL
                                        )""")
            cursor.execute("""INSERT INTO players(player_name, password_player)
                                VALUES(?,?)""", (txt_username, txt_password))

            conn.commit()
            cursor.close()
            conn.close()
            self.popup_register_window("Added To Database")
        except:
            self.popup_register_window("Cannot add to database")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    NewPlayer = QtWidgets.QWidget()
    log = GuiRegister()
    log.register_window(NewPlayer)
    NewPlayer.show()
    sys.exit(app.exec_())
