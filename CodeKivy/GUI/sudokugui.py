import psycopg2
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.vector import Vector

from core import Colors
from logic import DepthFirst, Blink, Movement, GridCheck
from logic.checker import Checker
from .key import Number
from .subgrid import SubGrid
from kivy.uix.label import Label
from kivy.uix.accordion import Accordion, AccordionItem
from os.path import join
from kivy.storage.jsonstore import JsonStore

class WindowManager(ScreenManager):
    pass


class SignInWindow(BoxLayout, Screen):
    def add_user(self, username, password):
        with open ('players.json') as players_file:
            players = json.load(file)
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


class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)

        self.rows = 3
        self.cols = 3

        self.spacing = 2

        self.selected = None

        self.grid = []
        self.block = {}
        self.row = {}
        self.col = {}

        self.depth_first = DepthFirst(self.grid, self.block, self.row, self.col, callback=self.reset_algorithm, dramatic=False)

        Window.bind(on_key_up=self._on_key_up, on_key_down=self._on_key_down)

        for i in range(self.rows * self.cols):
            subgrid = SubGrid(callback=self.callback)

            block = [i % self.cols, int(i / 3)]
            self.block[tuple(block)] = []

            for tile in subgrid.children:
                tile.block = block
                self.block[tuple(block)].append(tile)

            self.add_widget(subgrid)

        # initialization
        for i in range(9):
            self.grid.append([None] * 9)

            self.row[i] = []
            self.col[i] = []

        self.movement = Movement(self.grid)

        # grid fill and data identification
        for subgrid_no, subgrid in enumerate(self.children):

            block = Vector(subgrid_no % 3, int(subgrid_no / 3))
            for tile_no, tile in enumerate(subgrid.children):
                x = int(tile_no / 3) + block.y * 3
                y = tile_no % 3 + block.x * 3

                # flips
                x = (x * -1) + (9 - 1)
                y = (y * -1) + (9 - 1)

                tile.coords = [x, y]

                self.row[x].append(tile)
                self.col[y].append(tile)

                self.grid[x][y] = tile

class SaveGame():
    pass


kv = Builder.load_file("sudokugui.kv")


class SudokuGui(App):
    def build(self):
        return kv



if __name__ == "__main__":
    sudoku = SudokuGui()
    sudoku.run()
