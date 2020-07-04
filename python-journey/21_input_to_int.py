data = '10, 20, 30, 40, 50'

strings = data.split(',')
print(strings)

# map(), Make an iterator that computes the function using arguments from each of the iterables.
numbers = list(map(int, data.split(',')))
print(numbers)

sums = list(map(lambda x, y: x + y, [1, 2, 3], [2, 3, 4]))
print(sums)

