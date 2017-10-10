rows = 1
cols = 10

import random
def game(rows, cols):
    'een lekker spelletje mn jongen'

    table = (rows*cols-1)*[''] + ['B']
    random.shuffle(table)

    while True:
        pos = input('Voer hier je volgende positie in (format: x y): ')
        position = pos.split()
        if table[int(position[0])*cols + int(position[1])] == 'B':
            print('De bom ontploft in je bakkes!')
            break
        else:
            print('Er is hier geen bom te vinden mn jongen', pos)
print(game(rows, cols))
