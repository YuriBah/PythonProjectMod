#a
from itertools import count, cycle

for a in count(int(input('Введите число: '))):
    print(a)

#b
my_list = [1, 1, 2, 3, 4, 5, 5, 7, 8, 3, 10, 11, 1]

iter = cycle(my_list)
stop = " "
while stop != "x":
    print(next(iter), end = " ")
    stop = input()
    