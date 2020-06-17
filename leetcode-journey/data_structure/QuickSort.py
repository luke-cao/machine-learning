def dutch_flag_partition(pivot_index: int, A: list):
    if len(A) == 1:
        return A

    pivot = A[pivot_index]
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        if A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1
    return A, smaller, larger


def quick_sort(A):
    if len(A) == 0:
        return A

    smaller = []
    larger = []
    equal = []
    pivot = A[len(A) // 2]
    for i in A:
        if i < pivot:
            smaller.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            larger.append(i)
    return quick_sort(smaller) + equal + quick_sort(larger)

def quick_sort2(A):



test = [2, 3, 5, 6, 7, 45, 4, 0, 9, 5]
print(test)
print(quick_sort(test))