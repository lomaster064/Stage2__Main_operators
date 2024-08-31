a, b, c = map(int, input().split())

# if a == b == c:
#     print(3)
# elif a == b != c or a == c != b:
#     print(2)
# else:
#     print(0)

# второй вариант
if a == b and a == c:
    print('Все числа равны')
elif a == b and a != c or a == c and a != b:
    print('2 числа из набора равны')
else:
    print('Все числа разные')
