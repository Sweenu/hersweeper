import random
import itertools

import tabulate

from .utils import to_letters

tabulate.PRESERVE_WHITESPACE = True
EASY = 10
NORMAL = 20
HARD = 30
BOMB = u'\U0001F4A3'
FLAG = u'\u2691'


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
        elif self.is_revealed:
            if self.is_bomb:
                return BOMB
            else:
                return str(self.value) if self.value != 0 else ' '
        else:
            return ' . '


class Row:
    """A list containing 'nb_cols' Cells."""

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
    """A list containing 'nb_rows' Rows."""

    def __init__(self, nb_cols: int, nb_rows: int):
        self.nb_cols = nb_cols
        self.nb_rows = nb_rows
        self.__grid = [Row(nb_cols, i) for i in range(nb_rows)]

    def __str__(self):
        grid = tabulate.tabulate(self, tablefmt='fancy_grid')
        grid_with_headers = '   '
        for i in range(self.nb_cols):
            grid_with_headers += f'   {i + 1}  '

        grid_with_headers += '\n'
        turn = 1
        for i, line in enumerate(grid.split('\n')):
            if i % 2 != 0:
                grid_with_headers += f' {to_letters(i - turn)} ' + line + '\n'
                turn += 1
            else:
                grid_with_headers += '   ' + line + '\n'
        return grid_with_headers

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
            if tup != (cell.x, cell.y) and tup[0] >= 0 and tup[1] >= 0:
                try:
                    yield self[tup[1]][tup[0]]
                except IndexError:
                    pass


class Game:
    def __init__(self, grid: Grid, bomb_percentage: int):
        self.grid = grid
        self.bomb_percentage = bomb_percentage
        self.bombs = []
        self.revealed_cells = []

    def init(self):
        """Initalize the game's grid.

        Randomly spread bombs across the grid according to the chosen bomb
        percentage. Change the value of each cell accordingly.
        """
        nb_cells = self.grid.nb_cols * self.grid.nb_rows
        nb_bombs = round((nb_cells * self.bomb_percentage) / 100)
        for cell in self.grid.sample(nb_bombs):
            cell.is_bomb = True
            self.bombs.append(cell)

            for cell in self.grid.neighbor_cells(cell):
                cell.value += 1

    def __str__(self):
        return (f'Grid: {self.grid.nb_cols}x{self.grid.nb_rows}\n'
                f'Bomb percentage: {self.bomb_percentatge}')

    def propagate(self, cell: Cell):
        """Reveal cells neighboring the given cells.

        If a reaveled cell has a value of 0, propagate from this cell as well.
        """
        neighbors = self.grid.neighbor_cells(cell)
        for neighbor in neighbors:
            if not neighbor.is_revealed:
                self.reveal(neighbor)
                if neighbor.value == 0:
                    self.propagate(neighbor)

    def reveal(self, cell: Cell):
        """Reveal a cell and puts it in the revealed_cells list."""
        cell.is_revealed = True
        self.revealed_cells.append(cell)
