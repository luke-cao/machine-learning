from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, s):
        visited = [False] * len(self.graph)
        self.DFSUtil(s, visited)

    def DFSUtil(self, s, visited: list):
        visited[s] = True
        print(s, end=" ")
        for i in self.graph[s]:
            if not visited[i]:
                self.DFSUtil(i, visited)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.DFS(2)
