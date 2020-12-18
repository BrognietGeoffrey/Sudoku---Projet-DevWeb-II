"""import the file for the login window"""
from CodePyQt5.Gui.sudokuguilogin import *
"""import for the connection with the database and the creation of the window"""
import sqlite3
from PyQt5 import QtCore, QtWidgets, QtGui


class GuiRegister(object):
    """
    Create the register login
    """

    def window_open(self):
        """
        Change to login window when the button login is clicked
        pre : -
        post: -
        """
        self.window = QtWidgets.QMainWindow()
        self.change = GuiLogin()
        self.change.login_window(self.window)
        self.window.show()


    def register_window(self, Form):
        """
        pre:
            :param Form: the form with the widget for the register window
        post: -
        """

        """
        Size of the window
        """
        Form.setObjectName("Form")
        Form.setFixedSize(600, 400)

        """
        Shape of the register logo
        """
        self.tr = QtWidgets.QTextBrowser(Form) # tr mean textRegister for the logo section
        self.tr.setGeometry(QtCore.QRect(150, 10, 361, 61))
        self.tr.setText("REGISTER")
        self.tr.setObjectName("text_browser")

        self.glw = QtWidgets.QWidget(Form) # glw mean gridLayoutWidget
        self.glw.setGeometry(QtCore.QRect(100, 90, 431, 261))
        self.glw.setObjectName("grid_layout_widget")

        self.gl = QtWidgets.QGridLayout(self.glw) #gl mean gridLayout
        self.gl.setContentsMargins(0, 0, 0, 0)
        self.gl.setObjectName("grid_layout")

        """
        Shape of the input section
        """
        self.p_username = QtWidgets.QLabel(self.glw) # p_usermane mean parse_username
        self.p_username.setObjectName("p_username")
        self.gl.addWidget(self.p_username, 0, 0, 1, 1)
        self.p_username.setText("Username : ")

        self.p_password = QtWidgets.QLabel(self.glw) # p_password mean parse_password
        self.p_password.setObjectName("p_password")
        self.gl.addWidget(self.p_password, 1, 0, 1, 1)
        self.p_password.setText("Password : ")

        self.tp = QtWidgets.QLineEdit(self.glw) # tp mean textPassword
        self.tp.setObjectName("text_password")
        self.gl.addWidget(self.tp, 1, 1, 1, 1)

        self.tu = QtWidgets.QLineEdit(self.glw) # tu mean textUsername
        self.tu.setObjectName("text_username")
        self.gl.addWidget(self.tu, 0, 1, 1, 1)

        """
        Shape of the button return to login window and register
        """
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
        """
        Function for the button register wich refers to the function window_open()
        pre: -
        post: -
        """
        self.window_open()

    def popup_register_window(self, text):
        """
        Function for the button return to login window wich refers to the function window_open()
        pre: -
        post: -
        """
        popup_message = QtWidgets.QMessageBox()
        popup_message.setIcon(QtWidgets.QMessageBox.Critical)
        popup_message.setText("{}".format(text))
        popup_message.setInformativeText('{}'.format(text))
        popup_message.setWindowTitle("{}".format(text))

        popup_message.exec_()

    def database(self):
        """
        Function for the commit of new user in database

        pre: -
        post: -
        """
        if len(self.tp.text()) <= 1 : # If the field is empty, return popup avec invalid data
            self.popup_register_window('Enter Valid Data')
        else: # if not, do the insert to database
            try:
                txt_username = self.tu.text() # value of the username field
                txt_password = self.tp.text() # value of the password field

                conn = sqlite3.connect(r'../../CodePyQt5/Database/sudokudb.db') # Connection to database
                cursor = conn.cursor() # Connection between the database and the futur query selection
                cursor.execute("""CREATE TABLE IF NOT EXISTS players (
                                            player_id integer NOT NULL PRIMARY KEY, 
                                            player_name text NOT NULL, 
                                            password_player text NOT NULL
                                            )""")
                cursor.execute("""INSERT INTO players(player_name, password_player)
                                    VALUES(?,?)""", (txt_username, txt_password))
                conn.commit() # Commit to database
                cursor.close() # end query
                conn.close() # Close connection to database
                self.popup_register_window("Added To Database")
            except:
                self.popup_register_window("Cannot add to database")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    log = GuiRegister()
    log.register_window(Form)
    Form.show()
    sys.exit(app.exec_())
