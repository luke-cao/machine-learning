"""
underflow
"""
n1 = 0.1 + 0.2 - 0.3
n2 = 0.0
print(f'0.1 + 0.2 - 0.3 = {0.1 + 0.2 - 0.3}')
print(type(n1), type(n2))
print(n1 == n2)
print(abs(n1 - n2) < 1e-15)
