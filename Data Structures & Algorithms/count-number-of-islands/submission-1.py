class Solution:
    # this bfs visits an entire island that starts from the given row and col.
    def bfs(self, grid: list[list[str]], row: int, col: int, n: int, m: int):
        
        # we visit land by setting it to "0".
        grid[row][col] = "0"

        # visit cardinally adjacent neighbours if land exists there.
        if row < n - 1 and grid[row + 1][col] == "1":
            self.bfs(grid, row + 1, col, n, m)
        if col < m - 1 and grid[row][col + 1] == "1":
            self.bfs(grid, row, col + 1, n, m)
        if row > 0 and grid[row - 1][col] == "1":
            self.bfs(grid, row - 1, col, n, m)
        if col > 0 and grid[row][col - 1] == "1":
            self.bfs(grid, row, col - 1, n, m)

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        n, m = len(grid), len(grid[0])
        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1":
                    islands += 1

                    # this bfs call will visit an entire island.
                    self.bfs(grid, row, col, n, m)

        return islands