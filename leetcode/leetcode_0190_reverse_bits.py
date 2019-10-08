class Solution(object):
    # Pythonic way, easy to understand.
    def reverseBits(self, n):
        bit_str = f'{n:032b}'
        reverse_str = bit_str[::-1]
        return int(reverse_str, 2)


if __name__ == '__main__':
    input = '00000010100101000001111010011100'
    n = int(input, base=2)
    print(n)
    ret = Solution().reverseBits(n)
    print(f'{ret:032b}')