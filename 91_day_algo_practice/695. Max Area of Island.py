class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return 0
            if grid[r][c] == 0 or grid[r][c] == 2:
                return 0
            if grid[r][c] == 1:
                grid[r][c] = 2  # 已经走过标记为2 mark as visited
                area = 1

                area += dfs(grid, r + 1, c)
                area += dfs(grid, r - 1, c)
                area += dfs(grid, r, c + 1)
                area += dfs(grid, r, c - 1)
                return area

        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(grid, r, c))
        return max_area
