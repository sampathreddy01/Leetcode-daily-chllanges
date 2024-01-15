class Solution(object):
    def findMatrix(self, nums):
        l={}
        for j in nums:
            if j in l:
                l[j]+=1
            else:
                l[j]=1
        result=[]
        while l:
            row=[]
            keys_to_remove = list(l.keys())
            for j in keys_to_remove:
                row.append(j)
                l[j] -= 1
                if l[j] == 0:
                    l.pop(j)
            result.append(row)
        return result
