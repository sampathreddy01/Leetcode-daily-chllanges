class Solution(object):
    def rearrangeArray(self, nums):
        pos=[]
        neg=[]
        for j in nums:
            if j<0:
                neg.append(j)
            else:
                pos.append(j)
        n=len(nums)
        for i in range(n):
            if i%2==0:
                nums[i]=pos[i//2]
            else:
                nums[i]=neg[i//2]
        return nums
        
        
        
