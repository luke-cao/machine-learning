# class Solution:
#     def countAndSay(self, n: int) -> str:
#         ret = '1'
#         for _ in range(n - 1):
#             new_ret = ''
#             temp = {}
#             for i in range(len(ret)):
#                 if not temp:
#                     temp[ret[i]] = 1
#                 elif ret[i] in temp:
#                     temp[ret[i]] += 1
#                 else:
#                     new_ret += str(list(temp.values())[0]) + list(temp.keys())[0]
#                     temp = {ret[i]: 1}
#             if temp:
#                 new_ret += str(list(temp.values())[0]) + list(temp.keys())[0]
#             ret = new_ret
#         return ret


class Solution:
    def countAndSay(self, n: int) -> str:
        ret = '1'
        for _ in range(n - 1):
            new_ret = ''
            num, count = None, 0
            for i in ret:
                if num is None:
                    num, count = i, 1
                elif i == num:
                    count += 1
                else:
                    new_ret += str(count) + num
                    num, count = i, 1
            if count:
                new_ret += str(count) + num
            ret = new_ret
        return ret

print(Solution().countAndSay(6))