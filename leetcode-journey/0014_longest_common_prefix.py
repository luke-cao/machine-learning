from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = []
        for i in zip(*strs):
            if len(set(i)) == 1:
                common_prefix.append(i[0])
            else:
                break
        return ''.join(common_prefix)


print(Solution().longestCommonPrefix(["dog","racecar","car"]))
assert Solution().longestCommonPrefix(["flower","flow","flight"]) == "fl", Solution().longestCommonPrefix(["flower","flow","flight"])
