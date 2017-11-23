import urwid as u

def setup_grid(grid):
    display = []
    for row in grid:
        display.append(row)

    #width = int((loop.screen.get_cols_rows()[0] - 2) / 3)
    return u.GridFlow(display, 8, 1, 1, "left")

