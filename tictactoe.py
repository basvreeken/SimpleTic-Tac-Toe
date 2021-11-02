# Set the rules
valid_input = ['X', 'O', '_']
play = True

c = input('Enter cells: ')

for x in c:
    if x not in valid_input:
        print('Incorrect input')
        play = False

# Display the 3x3 grid
if play is True:
    print(f'''---------
| {c[0]} {c[1]} {c[2]} |
| {c[3]} {c[4]} {c[5]} |
| {c[6]} {c[7]} {c[8]} |
---------''')

    # Analyze the game state
    win_lines = []
    if c[0] == c[1] and c[0] == c[2]:
        win_lines.append(c[0])
    if c[3] == c[4] and c[3] == c[5]:
        win_lines.append(c[3])
    if c[6] == c[7] and c[6] == c[8]:
        win_lines.append(c[6])
    if c[0] == c[3] and c[0] == c[6]:
        win_lines.append(c[0])
    if c[1] == c[4] and c[1] == c[7]:
        win_lines.append(c[1])
    if c[2] == c[5] and c[2] == c[8]:
        win_lines.append(c[2])
    if c[0] == c[4] and c[0] == c[8]:
        win_lines.append(c[0])
    if c[2] == c[4] and c[2] == c[6]:
        win_lines.append(c[2])

    if abs(c.count('X') - c.count('O')) > 1 or \
            'X' in win_lines and 'O' in win_lines:
        print('Impossible')
    elif not win_lines:
        if '_' in c:
            print('Game not finished')
        else:
            print('Draw')
    else:
        print(win_lines[0] + ' wins')
