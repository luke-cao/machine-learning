data = [1, 3, [5, [7, 8]], 9, 11]
print(data)


def flatten_list(alist):
    ret = []
    for i in alist:
        if hasattr(i, '__iter__'):
            ret.extend(flatten_list(i))
        else:
            ret.append(i)
    return ret


print(flatten_list(data))

