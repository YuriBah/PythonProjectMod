old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [number for a, number in enumerate(old_list) if number > old_list[a - 1] and a != 0]
print(new_list)