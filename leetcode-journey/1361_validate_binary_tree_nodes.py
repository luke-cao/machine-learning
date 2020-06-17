from typing import List
import collections


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        seen = set()

        for arr in (leftChild, rightChild):
            for x in arr:
                if x != -1:
                    if x in seen:  # has two parents
                        return False
                    seen.add(x)

        if len(seen) != n - 1:
            return False


        root = (set(range(n)) - seen).pop()  # only one possible element


        q = collections.deque([root])

        while q:
            x = q.popleft()
            n -= 1  # use parameter as reverse counter for num nodes visited

            if leftChild[x] != -1:
                q.append(leftChild[x])
            if rightChild[x] != -1:
                q.append(rightChild[x])

        return n == 0


assert Solution().validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]) == True
assert Solution().validateBinaryTreeNodes(n = 2, leftChild = [1,0], rightChild = [-1,-1]) == False

assert Solution().validateBinaryTreeNodes(n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]) == False