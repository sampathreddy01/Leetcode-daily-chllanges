class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        l={}
        for j in arr:
            if j in l:
                l[j]+=1
            else:
                l[j]=1
        min_heap=[]
        for j in l.values():
            heapq.heappush(min_heap,j)
        while k>0:
            t=heapq.heappop(min_heap)
            if k>=t:
                k-=t
            else:
                heapq.heappush(min_heap,t-k)
                k=0
        return len(min_heap)
