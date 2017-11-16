import random

NB_COLUMNS = 5
NB_ROWS = 3
BOMB_PERCENTAGE = 20


class Game:
    def __init__(self, grid):
        self.grid = grid

    def init(self, bomb_percentage):
        for i in self.grid.nb_rows:
            for j in self.grid.nb_columns:
                if random.randint(0, 100) < bomb_percentage:
                    self.grid[i][j].bomb = True
                    for square in grid.neighbor_squares(i, j):
                        square.nb += 1


class Row:
    def __init__(self, nb):
        self.__row = [Square() for _ in range(nb)]

    def __repr__(self):
        return self.__row.__repr__()

    def __getitem__(self, j):
        return self.__row[j]


class Grid:
    def __init__(self, nb_columns, nb_rows):
        self.nb_columns = nb_columns
        self.nb_rows = nb_rows
        self.__grid = [Row(nb_columns) for _ in range(nb_rows)]

    def __repr__(self):
        return f'{self.nb_columns}x{self.nb_rows} grid'

    def __getitem__(self, i):
        return self.__grid[i]

    def neighbor_squares(self, i, j):
        pass


class Square:
    def __init__(self, nb_neighbor_bomb=0, bomb=False, flag=False):
        self.bomb = bomb
        self.flag = flag
        self.nb = nb_neighbor_bomb

    def __repr__(self):
        if self.bomb:
            return 'B'
        elif self.flag:
            return 'F'
        else:
            return str(self.nb)


def main():
    grid = Grid(NB_COLUMNS, NB_ROWS)
    game = Game(grid)
    game.init(BOMB_PERCENTAGE)


if __name__ == '__main__':
    main()
