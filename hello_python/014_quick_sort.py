def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot_idx = 0
    pivot = arr[pivot_idx]
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


array = [1, 3, 5, 7, 8, 3, 4]
print(quick_sort(array))
