# Напишите программу, удаляющую из текста все слова содержащие "абв". 

def ABV(loc_str): return ' '.join(filter(lambda e: e.find('абв') == -1, loc_str.split(' ')))

init_text ='Ехал грека через реку,абв видит грека — в реке рак.Сунул грека рукуабв в реку, рак за абв руку греку — цап!' 

print(init_text)

print(ABV(init_text))