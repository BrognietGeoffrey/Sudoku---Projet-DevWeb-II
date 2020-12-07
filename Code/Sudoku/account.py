from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label


"""
class NewAccount(Screen):
    name_player = ObjectProperty(None)
    password_player = ObjectProperty(None)
    email_player = ObjectProperty(None)

    def submit(self):
        if self.name_player.text != "" and self.password_player.text != "" and self.email_player.text.count("@") == 1 and self.email_player.text.count(".") > 0:
            if self.password_player != "":
                db.add_user


kv = Builder.load_file("account.kv")


class MainApp(App):
    def build(self):
        return kv
"""