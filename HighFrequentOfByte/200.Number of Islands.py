from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, r, c):
            # base case
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return
            # mark the 1 value is walked

            if grid[r][c] == "1":
                grid[r][c] = "2"
            else:  # 0是边界，2 已经走过，都需要返回
                return
            dfs(grid, r - 1, c)
            dfs(grid, r + 1, c)
            dfs(grid, r, c - 1)
            dfs(grid, r, c + 1)

        rows, cols = len(grid), len(grid[0])
        i_num = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    i_num += 1
                    dfs(grid, r, c)
        return i_num


if __name__ == "__main__":
    s = Solution()
    s.numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    )
