class Solution(object):
    def minOperations(self, nums):
        l={}
        for j in nums:
            if j in l:
                l[j]+=1
            else:
                l[j]=1
        res=0
        for j in l:
            if l[j]==1:
                return -1
            k1=l[j]%3
            k2=l[j]//3
            if k1:
                res+=1
            res+=k2
        return res

        
