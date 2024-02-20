class Solution(object):
    def furthestBuilding(self, h, bricks, ladders):
        # min_heap=[]
        # for i in range(1,len(heights)):
        #     diff=heights[i]-heights[i-1]
        #     if diff<=0:
        #         continue
        #     bricks-=diff
        #     heapq.heappush(min_heap,-diff)
        #     if bricks<0:
        #         if ladders==0:
        #             return i
        #         ladders-=1
        #         bricks+=-heapq.heappop(min_heap)
        # return len(heights)-1
        
        heap=[]
        heapify(heap)
        for i in range(len(h)-1):
            d=h[i+1]-h[i]
            if d>0:
                heappush(heap,d)
                if len(heap)>ladders:
                    bricks-=heappop(heap)
                    if bricks<0:
                        return i
        return len(h)-1
