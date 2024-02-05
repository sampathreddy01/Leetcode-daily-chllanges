class Solution(object):
    def firstUniqChar(self, s):
        l={}
        t=[0]*len(s)
        index=-1
        for j in s:
            if j in l:
                l[j]+=1
            else:
                l[j]=1
        for k in range(len(s)):
            t[k]=l[s[k]]
            if t[k]==1:
                index=k
                break
        return index
        
