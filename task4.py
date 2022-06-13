# Чисто для тренировки новый функций, ничего сложного. 
# Создайте два списка — один с названиями языков программирования, 
# другой — с числами от 1 до длины первого плюс 1. 

alphavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abc= {alphavit[i]:i+65 for i in range(len(alphavit))}

program = ['Python','C','Fortran','Java','Bash','PHP','Pascal','Basic','Lisp','Assembler','Prolog','Perl','Go']
numbers = list(range(1,len(program)+1))


def CostWord(local_str): return sum([abc[local_str[i]] for i in range(len(local_str))])


def MyGetTuples(list1,list2): return [(list1[i],list2[i].upper()) for i in range(len(list1))]


def MyFilter(local_list): return [list([CostWord(local_list[i][1]),local_list[i][1]]) \
                                  for i in range(len(local_list)) \
                                  if CostWord(local_list[i][1]) % local_list[i][0] == 0]


print(MyGetTuples(numbers,program))

print(MyFilter(MyGetTuples(numbers,program)))