n = int(input("Введите число: "))

raw_list = []

for i in range(1, n):
    for j in range(i+1, n):
        if n % (i + j) == 0:
            raw_list.append([i, j])

processed_list = []

for k in raw_list:
    for l in k:
        processed_list.append(l)

print(raw_list)
print(processed_list)

result = ''.join(map(str,processed_list))
print(result)