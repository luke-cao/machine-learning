from typing import List
from collections import defaultdict


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1 and len(trust) == 0:
            return 1
        trust_dict = defaultdict(list)
        for t in trust:
            trust_dict[t[0]].append(t[1])
        if len(trust_dict) == N:
            return -1
        judge = set()
        for idx, values in enumerate(trust_dict.values()):
            if idx == 0:
                judge = set(values)
            judge &= set(values)
            if len(judge) == 0:
                return -1
        return judge.pop() if len(judge) == 1 else -1


N = 1
trust = []
print(Solution().findJudge(N, trust))