class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        s=sum(nums)
        flag=True
        j=len(nums)-1
        res=-1
        while flag:
            t=nums[j]
            if(s-t<=t):
                j-=1
                s-=t
                if j<0:
                    flag=False
            else:
                res=s
                flag=False
        return res
        
