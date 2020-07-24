class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        for node1, node2 in prerequisites:
            adjacency[node2].append(node1)
            indegrees[node1] += 1
        queue = []
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
        while queue:
            pop_node = queue.pop(0)
            numCourses -= 1
            for next_node in adjacency[pop_node]:
                indegrees[next_node] -= 1
                if indegrees[next_node] == 0:
                    queue.append(next_node)
        return False if numCourses else True
