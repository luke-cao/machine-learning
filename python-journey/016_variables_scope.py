x = 300


def my_func():
    global x
    x = 200


my_func()
print(x)
