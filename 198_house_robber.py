class Solution(object):
    def rob(self, nums):
        n=len(nums)
        amount=[0]*n
        if n<3:
            return max(nums)
        amount[0]=nums[0]
        amount[1]=max(nums[0],nums[1])
        for j in range(2,n):
            amount[j]=max(amount[j-1],amount[j-2]+nums[j])
        return amount[n-1]
        
