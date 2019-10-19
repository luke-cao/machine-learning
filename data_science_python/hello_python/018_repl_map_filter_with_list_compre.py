numbers = [4, 2, 1, 6, 8, 7]


def square(x):
    return x ** 2


def is_odd(x):
    breakpoint()
    return bool(x % 2)


print(list(map(lambda x: x ** 2, numbers)))
print(list(filter(is_odd, numbers)))
print([i ** 2 for i in numbers])
print([i for i in numbers if i % 2])


