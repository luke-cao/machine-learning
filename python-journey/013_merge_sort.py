from typing import List


def merge_sort(arr: List):
    """
    divide and conquer algorithm
    :param arr:
    :return:
    """

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right, arr.copy())


def merge(left, right, arr: List):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            arr[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            arr[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    if left_cursor < len(left):
        arr[left_cursor + right_cursor:] = left[left_cursor:]
    elif right_cursor < len(right):
        arr[left_cursor + right_cursor:] = right[right_cursor:]
    return arr


array = [1, 3, 5, 7, 8, 3, 4]
print(merge_sort(array))