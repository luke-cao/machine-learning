class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lookup = dict()
        for i in s:
            if i in lookup:
                lookup[i] += 1
            else:
                lookup[i] = 1
        for i in t:
            if lookup.get(i, 0):
                lookup[i] -= 1
            else:
                return False
        return True


s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))
s = "rat"
t = "car"
print(Solution().isAnagram(s, t))