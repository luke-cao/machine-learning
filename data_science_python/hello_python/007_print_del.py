data = [1, 3, 5, 7, 9, 11]

for i in range(len(data)):
    print(data[i])  # index out of range exception
    if i == 3:
        del data[i]

print(data)