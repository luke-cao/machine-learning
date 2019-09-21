def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        while cursor < arr[pos - 1] and pos > 0:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = cursor
    return arr


array = [1, 3, 5, 7, 8, 3, 4]
print(insertion_sort(array))