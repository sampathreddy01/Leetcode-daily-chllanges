class Solution(object):
    def cherryPickup(self, grid):
        ROW_NUM = len(grid)
        COL_NUM = len(grid[0])

        dp = [[[0] * COL_NUM for _ in grid[0]] for _ in grid]
        for i in range(COL_NUM):
            for j in range(COL_NUM):
                dp[-1][i][j] = grid[-1][i] if i == j else grid[-1][i] + grid[-1][j]

        for k in range(ROW_NUM - 2, -1, -1):
            row = grid[k]
            for i in range(COL_NUM):
                for j in range(i, COL_NUM):
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if 0 <= i + di < COL_NUM and 0 <= j + dj < COL_NUM:
                                if i == j:  # they can only pickup once
                                    dp[k][i][j] = max(dp[k][i][j], dp[k + 1][i + di][j + dj] + row[i])
                                else:
                                    dp[k][i][j] = max(dp[k][i][j], dp[k + 1][i + di][j + dj] + row[i] + row[j])
        return dp[0][0][COL_NUM - 1]
        
