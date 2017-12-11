import re

import click

from hersweeper import core

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

        grid = core.Grid(int(size.group(1)), int(size.group(2)))
        self.game = core.Game(grid, bomb_percentage)
        self.game.init()

    def run(self):
        while True:
            print("What's your next move? (h for help)")
            input(self.prompt)
            


@click.command()
@click.command('--graphic', '-g', is_flag=True,
               help='Run the game in terminal graphic mode')
def main(graphic):
    if graphic:
        print('Not implemented yet.')
    else:
        game = CommandLine()

    game.setup_game()
    game.run()


if __name__ == '__main__':
    main()
