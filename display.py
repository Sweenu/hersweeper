import urwid



def grid_into_widget(grid):
    rows = []
    for row in grid:
        cells = []
        for cell in row:
            text = str(cell.nb) if cell.is_revealed else ' '
            if cell.is_flagged:
                text = FLAG

            cells.append(urwid.Text(text))

        rows.append(urwid.Columns(cells))

    return rows

lbox = urwid.ListBox()
loop = urwid.MainLoop()
