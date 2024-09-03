my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

count = len(my_list)
ind = 0

while ind < count:
    value = my_list[ind]

    if value > 0:
        print(value)
        ind = ind + 1
    elif value == 0:
        ind = ind + 1
        continue
    else:
        break
        # ind = ind + 1
        # continue
        # если хотим перебрать список до конца
