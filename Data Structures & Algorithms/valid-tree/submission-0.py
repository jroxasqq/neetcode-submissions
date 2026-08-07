class Solution:
    def hasCycle(
        self,
        node: int,
        parent: int,
        graph: list[list[int]],
        visited: list[int]
    ):
        visited[node] = True

        for neighbour in graph[node]:
            if not visited[neighbour]:
                if self.hasCycle(neighbour, node, graph, visited):
                    return True
            elif neighbour != parent:
                # this condition is satisfied if this neighbour has been
                # visited before and is not the direct parent of this node.
                # this is because of the undirected graph nature, we don't
                # consider node <-> neighbour a cycle.
                return True

        return False

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph  = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        # this only detects cycles for the connected component that has
        # the node 0 in it. for cycles in other components, the isConnected
        # condition will handle that (for this specific question only).
        hasNoCycles = not self.hasCycle(0, -1, graph, visited)
        
        isConnected = all(visited)

        # valid trees are defined as graphs that are connected and
        # contains no cycles.
        return hasNoCycles and isConnected