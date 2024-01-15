class Solution(object):
    def lengthOfLIS(self, nums):
        l=[1]*len(nums)
        for j in range(1,len(nums)):
            for k in range(j):
                if(nums[k]<nums[j]):
                    l[j]=max(l[j],l[k]+1)
        return max(l)
        
