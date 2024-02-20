class Solution(object):
    def largestDivisibleSubset(self, nums):
        nums.sort()
        n=len(nums)
        dp=[1]*n
        size,index=1,0
        for j in range(1,n):
            for k in range(j):
                if(nums[j]%nums[k]==0):
                    dp[j]=max(dp[j],dp[k]+1)
                    if dp[j]>size:
                        size=dp[j]
                        index=j
        max_val=nums[index]
        # print(dp)
        # print(index,max_val)
        res=[]
        for i in range(index, -1, -1):
            if max_val % nums[i] == 0 and dp[i] == size:
                res.append(nums[i])
                max_val = nums[i]
                size -= 1
        return res
