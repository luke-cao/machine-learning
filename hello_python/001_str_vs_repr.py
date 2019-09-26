"""
__str__ vs __repr__

__str__: end user readable
__repr__: actual object
"""

import datetime


class C:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return f'C({self.val})'


if __name__ == '__main__':
    c = C(10)
    print(c)  # 10
    print(str(c))  # 10
    print(repr(c))  # C(10)
    print()

    print('hello')
    print(str('hello'))
    print(repr('hello'))

    print()
    today = datetime.datetime.today()
    print(today)
    print(str(today))
    print(repr(today))