numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = False

for i in numbers:
    if i == 1:
        continue

    is_prime = False
    for j in range(2, i):
        if i % j == 0:
            is_prime = True
            not_primes.append(i)
            break

    if is_prime == False:
        primes.append(i)
