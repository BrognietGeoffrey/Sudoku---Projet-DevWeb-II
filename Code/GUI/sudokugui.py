from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class WindowManager(ScreenManager):
    pass


class SignInWindow(BoxLayout, Screen):
    pass
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        
        user_name = self.ids.username_field
        password = self.ids.password_field

        uname = user_name.text
        pwd = password.text

        if uname == '' or pwd == '':
            print('username and/ or password required')
        else:
            if uname == 'admin' and pwd == 'admin':
                print("Bienvenue")
"""


class RegisterWindow(BoxLayout, Screen):
    pass


class PlayerWindow(BoxLayout, Screen):
    pass


class GameWindow(BoxLayout, Screen):
    pass


kv = Builder.load_file("sudokugui.kv")


class SudokuGui(App):
    def build(self):
        return kv


if __name__ == "__main__":
    sudoku = SudokuGui()
    sudoku.run()