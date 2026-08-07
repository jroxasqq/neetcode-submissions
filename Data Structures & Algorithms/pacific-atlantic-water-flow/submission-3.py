class Solution:
    def dfs(
        self,
        heights: List[List[int]],
        row: int,
        col: int,
        n_rows: int,
        n_cols: int,
        ocean: set[tuple[int, int]]
    ):
        coords = (row, col)

        if coords in ocean:
            return

        ocean.add(coords)

        if row > 0 and heights[row - 1][col] >= heights[row][col]:
            self.dfs(heights, row - 1, col, n_rows, n_cols, ocean)
        if col > 0 and heights[row][col - 1] >= heights[row][col]:
            self.dfs(heights, row, col - 1, n_rows, n_cols, ocean)
        if row < n_rows - 1 and heights[row + 1][col] >= heights[row][col]:
            self.dfs(heights, row + 1, col, n_rows, n_cols, ocean)
        if col < n_cols - 1 and heights[row][col + 1] >= heights[row][col]:
            self.dfs(heights, row, col + 1, n_rows, n_cols, ocean)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # solution,
        # find all the nodes that can flow TOWARDS the pacific ocean
        # find all the nodes that can flow TOWARDS the atlantic ocean
        # get the intersection of the above 2 sets of nodes

        pacific, atlantic = set(), set()
        n_rows, n_cols = len(heights), len(heights[0])

        for col in range(n_cols):
            
            # top border cells
            self.dfs(heights, 0, col, n_rows, n_cols, pacific)

            # bottom border cells
            self.dfs(heights, n_rows - 1, col, n_rows, n_cols, atlantic)

        for row in range(n_rows):

            # left border cells
            self.dfs(heights, row, 0, n_rows, n_cols, pacific)
            
            # right border cells
            self.dfs(heights, row, n_cols - 1, n_rows, n_cols, atlantic)

        return [list(coord) for coord in pacific.intersection(atlantic)]