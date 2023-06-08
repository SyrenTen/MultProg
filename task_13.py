from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from kivy.core.window import Window

from random import randint

Window.size = (500, 500)
Window.clearcolor = (0 / 255, 0 / 255, 0 / 255, 1)


# у нас будет куча клеток(кнопок) и взаимодействия с ними поэтому создаем подскласс
class Cell(Button):
    def __init__(self, **kwargs):
        super().__init__()
        self.size = (90, 90)
        self.background_normal = 'cell.png'
        self.flagged = False
        self.mined = False
        self.count_mined = 0

    def place_flag(self):
        if self.flagged:
            self.background_normal = 'flag.png'
        else:
            self.background_normal = 'cell.png'


class Minesweeper(GridLayout):
    def __init__(self, **kwargs):
        super().__init__()
        self.rows = 9
        self.cols = 9
        self.cells = []
        self.create_buttons()
        self.create_mines()

    def create_buttons(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.add_widget(Cell())

    def create_mines(self):
        mine_pos = []
        while len(mine_pos) < 10: # expected type list но все норм если len(mine_pos)
            pos = (randint(0, self.rows), randint(0, self.cols))
            if pos not in mine_pos:  # нужно же 10 мин
                mine_pos.append(pos)
            cell = self.cells  # AttributeError надо поправить
            cell.mined = True  # теперь эти клетки - мины







class GameMinesweeper(App):
    def build(self):
        return Minesweeper()


if __name__ == '__main__':
    GameMinesweeper().run()
