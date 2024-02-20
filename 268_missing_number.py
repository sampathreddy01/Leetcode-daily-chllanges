class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        ex_su=n*(n+1)/2
        total_sum=sum(nums)
        return ex_su-total_sum
