from functools import reduce

def new_list(a, b):
    return a * b

my_list = [x for x in range(100, 1000) if x % 2 == 0]
print(reduce(new_list, my_list))