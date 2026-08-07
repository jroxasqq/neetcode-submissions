class Solution:
    def hasCycle(self, label, graph, visited, path):

        # if this label was found again on this same path, there's a cycle.
        if path[label]:
            return True

        # if visited before we've not terminated in canFinish(), thus we
        # terminate DFS here as there was no cycle previous found there.
        if visited[label]:
            return False
        
        visited[label] = True
        path[label] = True

        for neighbour in graph[label]:
            if self.hasCycle(neighbour, graph, visited, path):
                return True
        
        # reset the path for the next loop iteration in canFinish() by
        # setting values back to False as we backtrack in recursion.
        path[label] = False

        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            u, v = prereq
            graph[v].append(u)

        print(graph)

        # each loop iteration we create a new path but keep running visited list.
        visited, path = [False] * numCourses, [False] * numCourses
        for label in range(numCourses):
            if not visited[label] and self.hasCycle(label, graph, visited, path):
                return False
        
        return True