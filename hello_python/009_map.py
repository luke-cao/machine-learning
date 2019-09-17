data = [1, 3, 5, 7, 9]


def f(x):
    return x ** 2


squares = map(f, data)
print(type(squares))
print(squares)
print(list(squares))