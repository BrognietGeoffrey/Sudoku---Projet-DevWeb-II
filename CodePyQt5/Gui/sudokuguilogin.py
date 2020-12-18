"""Import the files for register and player window"""
from CodePyQt5.Gui.sudoku_gui_register import *
from CodePyQt5.Gui.sudoku_gui_player import *
"""Import for the creation of window and the connection  """
from PyQt5 import QtCore, QtWidgets, QtGui
import sqlite3


"""
Variables for the login function
"""
username = ""
password = ""


class GuiLogin(object):
    """
    Create the window login
    """
    def window_open(self):
        """
        Change to register window when the button register is clicked
        pre : -
        post: -
        """
        self.window = QtWidgets.QMainWindow()
        self.changeRegister = GuiRegister()
        self.changeRegister.register_window(self.window)
        self.window.show()
        Form.hide()

    def second_window_open(self):
        """
        Change to player window when the login is completed
        pre : -
        post: -
        """
        self.window = QtWidgets.QWidget()
        self.changePlayer = PlayerWindow()
        self.changePlayer.setup_gui(self.window)
        self.window.show()
        Form.hide()

    def login_window(self, Form):
        """
        pre :
            :param Form: the form with the widget for the login window
        post: -
        """

        """
        Size of window
        """
        Form.setObjectName("Form")
        Form.setFixedSize(600, 400)

        """
        Shape of the Login logo
        """
        self.tl = QtWidgets.QTextBrowser(Form) # tl mean textlogin
        self.tl.setGeometry(QtCore.QRect(150, 10, 361, 61))
        self.tl.setText("LOGIN")
        self.tl.setObjectName("text_browser")

        self.glw = QtWidgets.QWidget(Form) # glw mean gridLayoutWidget
        self.glw.setGeometry(QtCore.QRect(100, 90, 431, 261))
        self.glw.setObjectName("grid_layout_widget")

        self.gl = QtWidgets.QGridLayout(self.glw) # gl mean gridLayout
        self.gl.setContentsMargins(0, 0, 0, 0)
        self.gl.setObjectName("grid_layout")

        """
        Shape of the input section
        """

        self.p_username = QtWidgets.QLabel(self.glw) # p_username mean parse_username
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

        self.tu = QtWidgets.QLineEdit(self.glw)  # tu mean textUsername
        self.tu.setObjectName("text_username")
        self.gl.addWidget(self.tu, 0, 1, 1, 1)


        """
        Shape of the button Login and register
        """
        self.button_login = QtWidgets.QPushButton(self.glw)
        self.button_login.setStyleSheet("background-color: rgb(15, 15, 15; color:\'white\'")
        self.button_login.setObjectName("button_login")
        self.button_login.setText("LOGIN")
        self.gl.addWidget(self.button_login, 2, 1, 1, 1)

        self.button_register = QtWidgets.QPushButton(self.glw)
        self.button_register.setStyleSheet("background-color: rgb(20, 20, 20")
        self.button_register.setObjectName("button_register")
        self.button_register.setText("REGISTER")
        self.gl.addWidget(self.button_register, 3, 1, 1, 1)

        self.button_login.clicked.connect(self.button_login_action)
        self.button_register.clicked.connect(self.button_register_action)

    def popup_login_window(self, text):
        """
        Function for the popup when login failed
        pre:
            :param text: Text for the popup
        post: -
        """
        popup_message = QtWidgets.QMessageBox()
        popup_message.setIcon(QtWidgets.QMessageBox.Critical)
        popup_message.setText("{}".format(text))
        popup_message.setInformativeText('{}'.format(text))
        popup_message.setWindowTitle("{}".format(text))

        popup_message.exec_()

    def button_register_action(self):
        """
        Function for the button register wich refers to the function window_open()
        pre: -
        post: -
        """
        self.window_open()

    def button_login_action(self):
        """
        Function who analyse the entry of the user and connected him if the user is in the records
        pre: -
        post: -
        """
        if len(self.tp.text()) <= 1:
            self.popup_login_window('Enter Valid Data')
        else:
            username = self.tu.text()
            password = self.tp.text()

            conn = sqlite3.connect(
                r'../../CodePyQt5/Database/sudokudb.db')
            cursor = conn.cursor()

            cursor.execute("SELECT player_name, password_player FROM players")
            val = cursor.fetchall()

            if len(val) >= 1:
                for x in val:
                    if username in x[0] and password in x[1]:
                        self.second_window_open()
                    else:
                        pass
            else:
                print("User Not Found")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    log = GuiLogin()
    log.login_window(Form)
    Form.show()
    sys.exit(app.exec_())



