from typing import List
from collections import defaultdict


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagrams = defaultdict(list)
#         for word in strs:
#             key = ''.join(sorted(word))
#             anagrams[key].append(word)
#         return [words for words in anagrams.values()]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            count = [0 for _ in range(26)]
            for c in word:
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)].append(word)
        return [words for words in anagrams.values()]


input = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(input))