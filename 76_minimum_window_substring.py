import math
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        if len(s)<len(t):
            return ''
        res=[-1,-1]
        min_len=float('inf')
        con=Counter(t)
        l={}
        have=0
        left=0
        need=len(con)
        for i,j in enumerate(s):
            if j in l:
                l[j]+=1
            else:
                l[j]=1
            if l[j]==con[j]:
                have+=1
            while have==need:
                if i-left+1<min_len:
                    min_len=i-left+1
                    res[0]=left
                    res[1]=i
                l[s[left]]-=1
                if s[left] in con and con[s[left]]>l[s[left]]:
                    have-=1
                left+=1
        if min_len==float('inf'):
            return ''
        else:
            return s[res[0]:res[1]+1]    
