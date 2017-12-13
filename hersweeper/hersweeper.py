#!/usr/bin/env python
import re
import os

import click

from core import Game, Grid
from util import to_number

EASY = 10
NORMAL = 20
HARD = 30


class CommandLine:
    def __init__(self, prompt='--> '):
        self.prompt = prompt

    def setup_game(self):
        print('Size of grid (in the form <cols>x<rows>) [7x10]')
        size = re.match(r'(\d+)x(\d+)', input(self.prompt) or '7x10')

        print('Difficulty of the game (easy, normal or hard) [normal]')
        difficulty = input(self.prompt) or 'normal'
        if difficulty == 'easy':
            bomb_percentage = EASY
        elif difficulty == 'hard':
            bomb_percentage = HARD
        else:
            bomb_percentage = NORMAL

        grid = Grid(int(size.group(1)), int(size.group(2)))
        self.game = Game(grid, bomb_percentage)
        self.game.init()

    @staticmethod
    def _process_input(move):
        raw_x = ''.join([char for char in move if char.isalpha()])
        raw_y = ''.join([char for char in move if char.isdigit()])
        return to_number(raw_x), int(raw_y) - 1

    def print_help(self):
        help = ("To select a cell, type the cell's position in the form 'a3' "
                "or '8h'.\n"
                "To flag a cell, type 'flag <cell position>' or 'unflag' to "
                "unflag a cell.\n"
                "To get the rules, type 'rules'.\n"
                "Type quit (or exit) to quit the game.\n")
        print(help)

    def run(self):
        # TODO: clean this mess
        print(self.game.grid, end='\n\n')
        print("What's your next move? (h for help)")
        nb_cell_total = self.game.grid.nb_cols * self.game.grid.nb_rows

        while True:
            user_input = input(self.prompt)
            if user_input in ('h', 'help'):
                self.print_help()
                continue
            elif user_input in ('quit', 'exit'):
                os.exit(0)
            else:
                try:
                    x, y = self._process_input(user_input)
                    cell = self.game.grid[x][y]
                except ValueError as e:
                    print(e.args[0])
                    continue

                if cell.is_bomb:
                    for bomb in self.game.bombs:
                        self.game.reveal(bomb)
                    return False
                elif cell.value == 0:
                    self.game.propagate(cell)

                self.game.reveal(self.game.grid[x][y])
                nb_revealed_cells = len(self.game.revealed_cells)
                if len(self.game.bombs) + nb_revealed_cells == nb_cell_total:
                    return True

            print(self.game.grid, end='\n\n')
            print("What's your next move? (h for help)")


@click.command()
@click.option('--graphic', '-g', is_flag=True,
              help='Run the game in terminal graphic mode')
def main(graphic):
    if graphic:
        print('Not implemented yet.')
    else:
        game = CommandLine()

    game.setup_game()
    has_win = game.run()
    print(game.game.grid, end='\n\n')
    if has_win:
        print('You won!')
    else:
        print('Meh, you could have done better...')


if __name__ == '__main__':
    main()
