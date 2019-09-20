import datetime


def bubble_sort(arr):
    start = datetime.datetime.today()
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end = datetime.datetime.today()
    print(f'bubble_sort: {end - start}')
    return arr


def bubble_sort2(arr):
    start = datetime.datetime.today()
    n = len(arr)

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    x = -1
    swapped = True
    while swapped:
        swapped = False
        x += 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
    end = datetime.datetime.today()
    print(f'bubble_sort2: {end - start}')
    return arr


array = [1, 3, 5, 7, 8, 3, 4]
print(bubble_sort(array))
print(bubble_sort2(array))
