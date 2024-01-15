class Solution(object):
    def minSteps(self, s, t):
        l={}
        for j in s:
            if j in l:
                l[j]+=1
            else:
                l[j]=1
        for j in t:
            if j in l:
                l[j]-=1
            else:
                l[j]=-1
        res=0
        for j in l:
            if l[j]<0:
                res=res-l[j]
        return res
        
