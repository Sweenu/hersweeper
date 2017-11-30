import re

import core
import display

EASY = 10
NORMAL = 20
HARD = 30


def main():
    prompt = '--> '

    print('Size of grid (in the form <cols>x<rows>) [7x10]')
    size = re.match(r'(\d+)x(\d+)', input(prompt) or '7x10')

    print('Difficulty of the game (easy, normal or hard) [normal]')
    difficulty = input(prompt) or 'normal'
    if difficulty == 'easy':
        bomb_percentage = EASY
    elif difficulty == 'hard':
        bomb_percentage = HARD
    else:
        bomb_percentage = NORMAL

    game = core.Game(core.Grid(int(size.group(1)), int(size.group(2))),
                     bomb_percentage)
    game.init()

    print(game.grid)


if __name__ == '__main__':
    main()
