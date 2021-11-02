finished = False
grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
turn = 'O'


def show_grid():
    print(f'''---------
| {grid[0][0]} {grid[0][1]} {grid[0][2]} |
| {grid[1][0]} {grid[1][1]} {grid[1][2]} |
| {grid[2][0]} {grid[2][1]} {grid[2][2]} |
---------''')


def analyze_state():
    global finished
    win_lines = []
    if grid[0][0] == grid[0][1] and grid[0][0] == grid[0][2] and grid[0][0] \
            != ' ':
        win_lines.append(grid[0][0])
    if grid[1][0] == grid[1][1] and grid[1][0] == grid[1][2] and grid[1][0] \
            != ' ':
        win_lines.append(grid[1][0])
    if grid[2][0] == grid[2][1] and grid[2][0] == grid[2][2] and grid[2][0] \
            != ' ':
        win_lines.append(grid[2][0])
    if grid[0][0] == grid[1][0] and grid[0][0] == grid[2][0] and grid[0][0] \
            != ' ':
        win_lines.append(grid[0][0])
    if grid[0][1] == grid[1][1] and grid[0][1] == grid[2][1] and grid[0][1] \
            != ' ':
        win_lines.append(grid[0][1])
    if grid[0][2] == grid[1][2] and grid[0][2] == grid[2][2] and grid[0][2] \
            != ' ':
        win_lines.append(grid[0][2])
    if grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2] and grid[0][0] \
            != ' ':
        win_lines.append(grid[0][0])
    if grid[0][2] == grid[1][1] and grid[0][2] == grid[2][0] and grid[0][2] \
            != ' ':
        win_lines.append(grid[0][2])

    total_x = [cell for row in grid for cell in row].count('X')
    total_y = [cell for row in grid for cell in row].count('O')

    if abs(total_x - total_y) >= 2:
        print(total_y)
        print(total_x)
        print('Impossible')
    if 'X' in win_lines and 'O' in win_lines:
        print('Impossible')
    elif win_lines:
        print(win_lines[0] + ' wins')
        finished = True
    elif total_x + total_y == 9:
        print('Draw')
        finished = True


def play(player):
    global grid
    passed_check = False
    while not passed_check:
        coords = input('Enter the coordinates: ').split()
        try:
            coords = [int(x) - 1 for x in coords]
        except ValueError:
            print('You should enter numbers!')
            continue
        if coords[0] > 2 or coords[1] > 2:
            print('Coordinates should be from 1 to 3!')
            continue
        elif grid[coords[0]][coords[1]] != ' ':
            print('This cell is occupied! Choose another one!')
            continue
        else:
            passed_check = True
            grid[coords[0]][coords[1]] = player
            show_grid()


show_grid()

while not finished:
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    play(turn)
    analyze_state()
