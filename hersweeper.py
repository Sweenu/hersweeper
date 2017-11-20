import random
import itertools

NB_COLS = 5
NB_ROWS = 5
BOMB_PERCENTAGE = 20


class Game:
    def __init__(self, grid):
        self.grid = grid

    def init(self, bomb_percentage):
        nb_squares = self.grid.nb_cols * self.grid.nb_rows
        nb_bombs = round((nb_squares * bomb_percentage) / 100)
        for square in self.grid.sample(nb_bombs):
            square.bomb = True

            for square in self.grid.neighbor_squares(square):
                square.nb += 1

    def __str__(self):
        return f'{self.grid.nb_cols}x{self.grid.nb_rows}'


class Row:
    def __init__(self, nb_cols, row_nb):
        self.__row = [Square(x=i, y=row_nb) for i in range(nb_cols)]

    def __str__(self):
        row = ''
        for square in self:
            row += f'| {str(square)} '

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
        grid = ''
        for row in self:
            grid += str(row) + '\n'

        return grid

    def __getitem__(self, y):
        return self.__grid[y]

    def sample(self, nb_squares):
        squares = set()
        while len(squares) < nb_squares:
            y = random.randint(0, self.nb_rows - 1)
            x = random.randint(0, self.nb_cols - 1)
            square = self[y][x]
            # no need to test if the square is already in the set. A set can
            # only hold one copy of an element by nature
            squares.add(square)

        return squares

    def neighbor_squares(self, square):
        neighboring_squares = itertools.product(range(square.x-1, square.x+2),
                                                range(square.y-1, square.y+2))
        for tup in neighboring_squares:
            if tup != (square.x, square.y):
                try:
                    yield self[tup[1]][tup[0]]
                except IndexError:
                    pass


class Square:
    def __init__(self, x, y, nb_neighbor_bomb=0,
                 bomb=False, flag=False, revealed=False):
        self.x = x
        self.y = y
        self.bomb = bomb
        self.flag = flag
        self.nb = nb_neighbor_bomb

    def __str__(self):
        if self.bomb:
            return 'B'
            # return u'\U0001F4A3'
        elif self.flag:
            return 'F'
            # return u'\u2691'
        else:
            return str(self.nb) if self.nb != 0 else ' '


def main():
    game = Game(Grid(NB_COLS, NB_ROWS))
    print(game.grid)
    game.init(BOMB_PERCENTAGE)
    print(game.grid)


if __name__ == '__main__':
    main()
