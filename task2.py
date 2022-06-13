# Крестики нолики
field = '123456789'

def PrintField(local_field):
    print('-' * 13)
    for i in range(3): 
        print(f'| {local_field[i*3]} | {local_field[i*3 + 1]} | {local_field[i*3 + 2]} |')
        print('-' * 13)

def MyInput(local_field):
    num = int(input('Введите позию, куда будете ходить 1 - 9: ')) 
    while True:
        if not ((0 < num) and (num < 10)):
            print('Ввели неправильное место не существующее на поле')
        elif not(local_field[num-1] in '123456789'): 
            print('Это поле уже занято другим игроком')
        else: return str(num)
        num = int(input('Введите позию, куда будете ходить 1 - 9:'))

def MyCheckGame(local_field): 
    win_patterns = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
                                                                                 
    if len(local_field.replace('X','').replace('O','')) == 0: return 'Ничья!'
    if 'XXX' in list(filter(lambda x: x,[local_field[win_patterns[i][0]]+\
                                         local_field[win_patterns[i][1]]+\
                                         local_field[win_patterns[i][2]] \
                                    for i in range(len(win_patterns))])):
        return 'Крестики победили'
    if 'OOO' in list(filter(lambda x: x,[local_field[win_patterns[i][0]]+\
                                         local_field[win_patterns[i][1]]+\
                                         local_field[win_patterns[i][2]] \
                                    for i in range(len(win_patterns))])):
        return 'Нолики победили '
    return 'None'

game_result = 'None'
x_turn = True # Х - ходят первые

while game_result == 'None':
    PrintField(field)
    if x_turn: 
        print('Ходят X')
        field = field.replace(MyInput(field),'X')
    else: 
        print('Ходят O')
        field = field.replace(MyInput(field),'O')
    game_result = MyCheckGame(field)
    x_turn = not x_turn

print('Игра окончена')
PrintField(field)
print(game_result)
