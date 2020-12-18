"""import the files for the login function and the game window"""
from CodePyQt5.Gui.sudokuguilogin import *
from CodePyQt5.Gui.gui import *
"""import for the connection with database and the creation of database"""
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class PlayerWindow(object):
    """
    Create player window
    """

    def window_open_game(self):
        """
        Change to game window when the button into game is clicked
        pre : -
        post: -
        """
        self.window = QtWidgets.QMainWindow()
        self.change_window = SudokuGUI()
        self.change_window.__init__()
        Form.hide()
        self.window.show()

    def setup_gui(self, Form):
        """
        pre :
            :param Form: the form with the widget for the login window
        post: -
        """

        """
        Size of window
        """
        Form.setObjectName("Form")
        Form.setFixedSize(435, 313)

        """
        SHape of window
        """
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setStyleSheet("QTableWidget {background-color:rgb(220, 220, 220)}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)

        """
        Bold the horizontal name
        """
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        """
        Place of item an button in the tableWidget
        """
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.btn_player_game = QtWidgets.QPushButton(self.tableWidget)
        self.btn_player_game.setGeometry(QtCore.QRect(266, 0, 142, 36))
        self.btn_player_game.setObjectName("Game")
        self.btn_player_game.setText("Into Game")
        self.btn_player_game.clicked.connect(self.window_open_game)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """
        Put in the tale all data from the table of database
        pre :
            :param Form: form of the database filled by database
        post: -
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Player Table"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Joueur"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Score"))

        try:
            connection = sqlite3.connect(r'../../CodePyQt5/Database/sudokudb.db') # Connection with the database
            cursor = connection.cursor()  # Connection between the database and the futur query

            sqlite_select_query = """SELECT player_name, player_score from classement""" # query of selection in database
            cursor.execute(sqlite_select_query) # execution of the query
            self.tableWidget.setRowCount(0) # set rows at 0
            for row, form in enumerate(cursor): # for the number of rows in database
                self.tableWidget.insertRow(row) # insert the number of rows
                for column, item in enumerate(form): # for the number of columns in database
                    self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(item))) # insert the number of columns
        except sqlite3.Error as e:
            return e

    def button_action(self):
        """
        Function for the button game wich refers to the function window_open_game()
        pre: -
        post: -
        """
        self.window_open_game()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = PlayerWindow()
    ui.setup_gui(Form)
    Form.show()
    sys.exit(app.exec_())