class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        dp = [[[-1]*(maxMove+1) for _ in range(n+1)] for _ in range(m+1)]
        def solve(row,col,move):
            if move<0:
                return 0
            if row<0 or row>=m or col<0 or col>=n:
                return 1
            if dp[row][col][move]!=-1:
                return dp[row][col][move]
            a=solve(row-1,col,move-1)
            b=solve(row+1,col,move-1)
            c=solve(row,col-1,move-1)
            d=solve(row,col+1,move-1)

            dp[row][col][move]=a+b+c+d
            return dp[row][col][move]%1000000007

        return solve(startRow,startColumn,maxMove)
        
        
