import urwid

BOMB = u'\U0001F4A3'
FLAG = u'\u2691'


def grid_into_widget(grid):
    rows = []
    for row in grid:
        cells = []
        for cell in row:
            text = str(cell.nb) if cell.is_revealed else ' '
            if cell.is_flagged:
                text = FLAG

            cells.append(urwid.Text(text))

        rows.append(cells)

    return rows

# lbox = urwid.ListBox(rows)

# loop = urwid.MainLoop(lbox)
