# Set the rules
valid_input = ['X', 'O', '_']
play = True

cells = input('Enter cells: ')

for x in cells:
    if x not in valid_input:
        print('Incorrect input')
        play = False

grid = [cells[0], cells[1], cells[2]], [cells[3], cells[4], cells[5]], [
    cells[6], cells[7], cells[8]]

# Display the 3x3 grid
if play is True:
    print(f'''---------
| {grid[0][0]} {grid[0][1]} {grid[0][2]} |
| {grid[1][0]} {grid[1][1]} {grid[1][2]} |
| {grid[2][0]} {grid[2][1]} {grid[2][2]} |
---------''')

    # Analyze the game state
    win_lines = []
    if grid[0][0] == grid[0][1] and grid[0][0] == grid[0][2]:
        win_lines.append(grid[0][0])
    if grid[1][0] == grid[1][1] and grid[1][0] == grid[1][2]:
        win_lines.append(cells[3])
    if grid[2][0] == grid[2][1] and grid[2][0] == grid[2][2]:
        win_lines.append(grid[2][0])
    if grid[0][0] == grid[1][0] and grid[0][0] == grid[2][0]:
        win_lines.append(grid[0][0])
    if grid[0][1] == grid[1][1] and grid[0][1] == grid[2][1]:
        win_lines.append(grid[0][1])
    if grid[0][2] == grid[1][2] and grid[0][2] == grid[2][2]:
        win_lines.append(grid[0][2])
    if grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2]:
        win_lines.append(grid[0][0])
    if grid[0][2] == grid[1][1] and grid[0][2] == grid[2][0]:
        win_lines.append(grid[0][1])

    # Handle players move
    passed_check = False
    err_mess = 'You should enter numbers!'
    while not passed_check:
        coords = input('Enter the coordinates: ').split()
        try:
            coords = [int(x) - 1 for x in coords]
            print(coords)
        except ValueError:
            print('You should enter numbers!')
            continue
        if coords[0] > 2 or coords[1] > 2:
            print('Coordinates should be from 1 to 3!')
            continue
        elif grid[coords[0]][coords[1]] != '_':
            print('This cell is occupied! Choose another one!')
            continue
        else:
            passed_check = True
            grid[coords[0]][coords[1]] = 'X'
            print(f'''---------
| {grid[0][0]} {grid[0][1]} {grid[0][2]} |
| {grid[1][0]} {grid[1][1]} {grid[1][2]} |
| {grid[2][0]} {grid[2][1]} {grid[2][2]} |
---------''')

    # if abs(cells.count('X') - cells.count('O')) > 1 or \
    #         'X' in win_lines and 'O' in win_lines:
    #     print('Impossible')
    # elif not win_lines:
    #     if '_' in cells:
    #         print('Game not finished')
    #     else:
    #         print('Draw')
    # else:
    #     print(win_lines[0] + ' wins')
