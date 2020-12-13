from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.label import Label
from kivy.uix.accordion import Accordion, AccordionItem


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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        btn2 = Button(
            text='New Game',
            size_hint=(.5, .25),
            pos_hint={'left': 0, 'top': 1}
        )
        """btn2.bind(on_press=self.change_screen_to_game())
        self.add_widget(btn2)"""



        for x in range(5):
            item = AccordionItem()
            item.add_widget(Label(text='Very big content\n' * 10))
            self.add_widget(item)


class GameWindow(BoxLayout, Screen):
    pass


class SaveGame():
    pass


kv = Builder.load_file("sudokugui.kv")


class SudokuGui(App):
    def build(self):
        return kv


if __name__ == "__main__":
    sudoku = SudokuGui()
    sudoku.run()
