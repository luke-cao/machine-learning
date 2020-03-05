from typing import List

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans


A = ["amazon","apple","facebook","google","leetcode"]
B = ["ec","oc","ceo"]
assert Solution().wordSubsets(A, B) == ["facebook","leetcode"]

A = ["amazon","apple","facebook","google","leetcode"]
B = ["lo","eo"]
assert Solution().wordSubsets(A, B) == ["google","leetcode"]

A = ["amazon","apple","facebook","google","leetcode"]
B = ["e","oo"]
assert Solution().wordSubsets(A, B) == ["facebook","google"]