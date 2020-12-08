from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class SignIn(BoxLayout):
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


class Account(App):
    def build(self):
        return SignIn()


if __name__ == "__main__":
    account = Account()
    account.run()

