import re

count = 0
for i in range(0, 10_000):
    ch = chr(i)
    if re.match(r'\d', ch):
        print(ch, end='')
        count += 1
print()
print(count)