from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        c： course
        """
        res = []
        indegrees = [0 for _ in range(numCourses)]
        adjacencies_list = [[] for _ in range(numCourses)]
        for c_later, c_former in prerequisites:
            adjacencies_list[c_former].append(c_later)
            indegrees[c_later] += 1
        queue = [c for c, indegree in enumerate(indegrees) if indegree == 0]
        while queue:
            pop_course = queue.pop(0)
            numCourses -= 1
            res.append(pop_course)
            for c in adjacencies_list[pop_course]:
                indegrees[c] -= 1
                if indegrees[c] == 0:
                    queue.append(c)
        return res if numCourses == 0 else None


assert Solution().findOrder(3, [[2,1],[1,0]]) == [0,1,2]