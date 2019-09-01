class C:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.val + other.val

    def __sub__(self, other):
        return self.val - other.val

    def __lt__(self, other):
        print(f'{self.val} - {other.val}')
        return self.val - other.val

    def __repr__(self):
        return f'C({self.val})'

    def __str__(self):
        return f'Hello, my value is {self.val}'


c1 = C(10)
c2 = C(20)
c3 = C(30)
c4 = C(40)
print(c1)  # Hello, my value is 10
print(repr(c1))  # C(10)
print(c1 + c2)  # 30
print(c1 - c2)  # -10
cs = [c4, c2, c1, c3]
print(cs)
cs.sort()
print(cs)