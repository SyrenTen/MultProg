from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

from kivy.core.window import Window

from random import randint

Window.size = (600, 600)  # для определения размера окна


class Cell(Button):  # клас Cell наследуется от класса Button
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mine = False  # является миной
        self.flagged = False  # для флажка
        self.opened = False  # клетка открыта
        self.background_normal = 'cell.png'

    def on_touch_down(self, touch):  # on_touch_down(touch), запускается при нажатии
        if self.collide_point(*touch.pos) and touch.button == 'right':  # collide_point для проверки в границах
            self.flagged = not self.flagged  # переключает True - False
            if self.flagged:
                self.background_normal = 'flag.png'
            else:
                self.background_normal = 'cell.png'
            return True

        if self.collide_point(*touch.pos) and touch.button == 'left' and self.flagged:
            return False  # возрращает False и предотвращает нажатие
        return super().on_touch_down(touch)  # если ничего выше не произошло - просто нажатие


class Minesweeper(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 9
        self.rows = 9
        self.cells = []
        self.mine_count = 10
        self.creating_buttons()
        self.creating_mines()
        self.counting_mines()

    def creating_buttons(self):
        for row in range(self.rows):
            cell_rc = []
            for col in range(self.cols):
                cell = Cell()
                cell.bind(on_release=self.button_clicked)  # on_release запускается при отпускании кнопки
                self.add_widget(cell)
                cell_rc.append(cell)
            self.cells.append(cell_rc)

    def creating_mines(self):
        mine_pos = []
        while len(mine_pos) < 10:
            pos = (randint(0, self.rows - 1), randint(0, self.cols - 1))
            if pos not in mine_pos:
                mine_pos.append(pos)
                cell = self.cells[pos[0]][pos[1]]
                cell.mine = True

    def counting_mines(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cells[row][col]
                if not cell.mine:
                    amount = 0
                    for i in range(max(0, row - 1), min(row + 2, self.rows)):
                        for j in range(max(0, col - 1), min(col + 2, self.cols)):
                            if self.cells[i][j].mine:
                                amount += 1
                    cell.mine_count = amount

    def button_clicked(self, cell):
        if cell.mine:
            self.game_end(False)  # если в клетке есть мина - конец игры
        else:
            cell.opened = True
            cell.text = str(cell.mine_count)
            cell.disabled = True  # блокирует взаимодействие с клеткой

            if cell.mine_count == 0:  # если в соседних клетках нет мин
                self.opening_neighbors(cell)  # вызывается октрытие клеток

            if self.check_win():
                self.game_end(True)

    def check_win(self):  # проверяет были ли открыты все клетки-не-мины
        for row in self.cells:
            for cell in row:
                if not cell.opened and not cell.mine:
                    return False
        return True

    def cell_pos(self, cell):  # для поиска позиции клетки
        for row in range(self.rows):
            for col in range(self.cols):
                if self.cells[row][col] == cell:
                    return row, col

    def opening_neighbors(self, cell):
        row, col = self.cell_pos(cell)
        for i in range(max(0, row - 1), min(row + 2, self.rows)):
            for j in range(max(0, col - 1), min(col + 2, self.cols)):
                adjacent_cell = self.cells[i][j]
                if not adjacent_cell.opened and not adjacent_cell.mine:
                    adjacent_cell.opened = True
                    adjacent_cell.text = str(adjacent_cell.mine_count)
                    adjacent_cell.disabled = True
                    if adjacent_cell.mine_count == 0:
                        self.opening_neighbors(adjacent_cell)

    def game_end(self, stat):
        if stat:  # то значение True
            message = 'Win!'
        else:
            for row in self.cells:
                for cell in row:
                    if cell.mine:
                        cell.background_normal = 'bomb.png'
                    else:  # открывает ячейки после поражения
                        cell.opened = True
                        cell.text = str(cell.mine_count)
                        cell.disabled = True
            message = 'Game over'

        game_button = Button(text='New game')
        game_button.bind(on_release=self.new_game)
        popup = Popup(title=message, title_align='center', content=game_button,
                      size_hint=(None, None), size=(150, 150))
        popup.open()

    def new_game(self, arg):  # начало новой игры, вызывается при нажатии кнопки
        self.clear_widgets()  # очищает виджеты
        self.cells = []
        self.creating_buttons()
        self.creating_mines()
        self.counting_mines()


class GameMinesweeper(App):
    def build(self):
        return Minesweeper()


if __name__ == '__main__':
    GameMinesweeper().run()
