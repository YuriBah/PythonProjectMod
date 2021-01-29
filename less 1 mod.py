from sys import argv

time, sum_work, prize,pay = argv[1:]

def simple_calc():
    time = float(input('Введите количество отработанных часов : '))
    sum_work = float(input('Введите суммы оплаты труда за 1 час : '))
    prize = float(input('Укажите размер премии - '))
    pay = time * sum_work
    return pay + prize

print(f'Размер заработной платы составил: {simple_calc() }')
