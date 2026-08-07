class Solution:
    def dfs(self, node: int, graph: list[list[int]], visited: set[int]):
        if node in visited:
            return
        
        visited.add(node)

        for neighbour in graph[node]:
            self.dfs(neighbour, graph, visited)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)

        components = 0
        visited = set()
        for node in range(n):
            prev_visited_count = len(visited)
            self.dfs(node, graph, visited)
            if len(visited) != prev_visited_count:
                components += 1

        return components