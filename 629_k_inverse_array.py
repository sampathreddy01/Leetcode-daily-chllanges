class Solution(object):
    def kInversePairs(self, n, k):
        # mod=10**9+7
        # max_conversions=n*(n-1)/2
        # if k>max_conversions:
        #     return 0
        # if k==0 or k==max_conversions:
        #     return 1
        # dp=[[0 for _ in range(k+1)] for _ in range(n+1)]
        # for i in range(1,n+1):
        #     dp[i][0]=1
        # dp[2][1]=1
        # for i in range(3,n+1):
        #     max_conv=min(k,(i)*(i-1)/2)
        #     for j in range(1,max_conv+1):
        #         dp[i][j]=dp[i-1][j]+dp[i][j-1]
        #         if j>=i:
        #             dp[i][j]-=dp[i-1][j-1]
        #     dp[i][j]=(dp[i][j]+mod)%mod
        # return dp[n][k]
