class Solution(object):
    def findErrorNums(self, nums):
        l={i:1 for i in range(1,len(nums)+1)}
        for j in nums:
            l[j]-=1
        missing, duplicate=0,0
        for j in l:
            if l[j]==1:
                missing=j
            if l[j]==-1:
                duplicate=j
        return [duplicate,missing]
