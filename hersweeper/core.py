import random
import itertools

import tabulate
tabulate.PRESERVE_WHITESPACE = True

EASY = 10
NORMAL = 20
HARD = 30
BOMB = u'\U0001F4A3'
FLAG = u'\u2691'


class Game:
    def __init__(self, grid, bomb_percentage):
        self.grid = grid
        self.bomb_percentage = bomb_percentage

    def init(self):
        nb_cells = self.grid.nb_cols * self.grid.nb_rows
        nb_bombs = round((nb_cells * self.bomb_percentage) / 100)
        for cell in self.grid.sample(nb_bombs):
            cell.is_bomb = True

            for cell in self.grid.neighbor_cells(cell):
                cell.value += 1

    def __str__(self):
        return (f'Grid: {self.grid.nb_cols}x{self.grid.nb_rows}\n'
                f'Bomb percentage: {self.bomb_percentatge}')

    def propagate(self, cell):
        neighbors = self.grid.neighbor_cells(cell)
        for neighbor in neighbors:
            if neighbor.value == 0:
                neighbor.is_revealed = True
                self.propagate(neighbor)


class Row:
    def __init__(self, nb_cols, row_nb):
        self.__row = [Cell(x=i, y=row_nb) for i in range(nb_cols)]

    def __str__(self):
        row = ''
        for cell in self:
            row += f'| {str(cell)} '

        row += '|'
        return row

    def __getitem__(self, x):
        return self.__row[x]


class Grid:
    def __init__(self, nb_cols, nb_rows):
        self.nb_cols = nb_cols
        self.nb_rows = nb_rows
        self.__grid = [Row(nb_cols, i) for i in range(nb_rows)]

    def __str__(self):
        return tabulate.tabulate(self, tablefmt='fancy_grid')

    def __getitem__(self, y):
        return self.__grid[y]

    def sample(self, nb_cells):
        cells = set()
        while len(cells) < nb_cells:
            y = random.randint(0, self.nb_rows - 1)
            x = random.randint(0, self.nb_cols - 1)
            cell = self[y][x]
            # no need to test if the cell is already in the set. A set can
            # only hold one copy of an element by nature
            cells.add(cell)

        return cells

    def neighbor_cells(self, cell):
        neighboring_cells = itertools.product(range(cell.x - 1, cell.x + 2),
                                              range(cell.y - 1, cell.y + 2))
        for tup in neighboring_cells:
            if tup != (cell.x, cell.y):
                try:
                    yield self[tup[1]][tup[0]]
                except IndexError:
                    pass


class Cell:
    def __init__(self, x, y, nb_neighbor_bombs=0,
                 is_bomb=False, is_flagged=False, is_revealed=False):
        self.x = x
        self.y = y
        self.is_bomb = is_bomb
        self.is_flagged = is_flagged
        self.value = nb_neighbor_bombs
        self.is_revealed = is_revealed

    def __str__(self):
        if self.is_flagged:
            return FLAG
        else:
            return str(self.value) if self.is_revealed else ' '
