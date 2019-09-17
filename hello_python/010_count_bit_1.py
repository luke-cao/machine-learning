def count_bits_is_1(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


x = 10
print(count_bits_is_1(x))
print(bin(x))