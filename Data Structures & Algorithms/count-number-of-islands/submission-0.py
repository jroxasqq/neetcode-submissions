class Solution:
    # this bfs visits the an island that starting from the given row and col.
    def bfs(self, grid: list[list[str]], row: int, col: int, n: int, m: int):
        if grid[row][col] == "0":
            return

        # we visit land by setting it to "0".
        grid[row][col] = "0"

        # visit cardinally adjacent neighbours if land exists.
        if row < n - 1 and grid[row + 1][col] == "1":
            self.bfs(grid, row + 1, col, n, m)
        if col < m - 1 and grid[row][col + 1] == "1":
            self.bfs(grid, row, col + 1, n, m)
        if row > 0 and grid[row - 1][col] == "1":
            self.bfs(grid, row - 1, col, n, m)
        if col > 0 and grid[row][col - 1] == "1":
            self.bfs(grid, row, col - 1, n, m)

    def numIslands(self, grid: List[List[str]]) -> int:
        # the proposed solution will be to graph the grid.
        # using the graph we visit each node and do a BFS at an unvisited
        # node while setting nodes to "visited" during a BFS.
        # each time we start a BFS will correspond to the number of 
        # connected components i.e. the number of islands.
        
        islands = 0
        n, m = len(grid), len(grid[0])
        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1":
                    islands += 1
                    self.bfs(grid, row, col, n, m)

        return islands