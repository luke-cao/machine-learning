class Solution:
    def countAndSay(self, n: int) -> str:
        value = '1'
        for i in range(2, n + 1):
            count_num = []
            char, count = value[0], 1
            for c in value[1:]:
                if c == char:
                    count += 1
                else:
                    count_num.append(str(count) + char)
                    char, count = c, 1
            count_num.append(str(count) + char)
            value = ''.join(count_num)
        return value


# class Solution:
#     def countAndSay(self, n: int) -> str:
#         ret = '1'
#         for _ in range(n - 1):
#             new_ret = ''
#             num, count = None, 0
#             for i in ret:
#                 if num is None:
#                     num, count = i, 1
#                 elif i == num:
#                     count += 1
#                 else:
#                     new_ret += str(count) + num
#                     num, count = i, 1
#             if count:
#                 new_ret += str(count) + num
#             ret = new_ret
#         return ret

print(Solution().countAndSay(4))