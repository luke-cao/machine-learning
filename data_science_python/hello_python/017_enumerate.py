"""
enumerate return tuples which contain count (defaults to 0) and value
the parameters: iterable, start
"""

numbers = [45, 22, 14, 65, 97, 72]
for i, num in enumerate(numbers):
    if num % 3 == 0 and num % 5 == 0:
        numbers[i] = 'fizzbuzz'
    elif num % 3 == 0:
        numbers[i] = 'fizz'
    elif num % 5 == 0:
        numbers[i] = 'buzz'
print(numbers)

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons, start=10)))