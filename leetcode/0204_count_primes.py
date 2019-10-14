import math

def countPrimes(n: int) -> int:
    primes = [True for _ in range(n)]

    for i in range(2, n):
        if i ** 2 >= n:
            break
        if primes[i]:
            for j in range(i, n):
                if i * j >= n:
                    break
                primes[i * j] = False
    # print(primes)
    return sum(primes[2:])


print(countPrimes(2))