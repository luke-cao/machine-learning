import numpy as np

class C:
    def __init__(self, matrix):
        self.matrix = matrix

    def __matmul__(self, other):
        entries = []
        for row in self.matrix:
            for column in other.matrix.T:
                sum = 0
                for i in range(len(row)):
                    sum += row[i] * column[i]
                entries.append(sum)
        m = np.array([entries]).reshape(self.matrix.shape[0], other.matrix.shape[1])
        return m


m1 = np.array([1, 2, 3, 4]).reshape((2, 2))
m2 = np.array([4, 3, 2, 1]).reshape((2, 2))
print(m1)
print(m2)
print(m1 @ m2)

c1 = C(m1)
c2 = C(m2)
print(c1 @ c2)
