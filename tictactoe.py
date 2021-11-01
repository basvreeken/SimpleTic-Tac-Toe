# Set the rules
valid_input = ['X', 'O', '_']
play = True

# Read a string of 9 symbols
c = input('Enter cells: ')

if len(c) != 9:
    print('Input too short')
    play = False

for x in c:
    if x not in valid_input:
        print('Incorrect input')
        play = False
        break

# Display the 3x3 grid
if play is True:
    print(f'''---------
| {c[0]} {c[1]} {c[2]} |
| {c[3]} {c[4]} {c[5]} |
| {c[6]} {c[7]} {c[8]} |
---------''')
