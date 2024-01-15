from collections import defaultdict

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        n=len(nums)
        dp=[defaultdict(int) for _ in range(n)]
        res=0
        for i in range(1,n):
            for j in range(i):
                diff=nums[i]-nums[j]
                dp[i][diff]+=1
                if diff in dp[j]:
                    dp[i][diff]+=dp[j][diff]
                    res+=dp[j][diff]
        return res
        
