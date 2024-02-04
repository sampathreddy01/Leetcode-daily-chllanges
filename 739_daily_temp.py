class Solution(object):
    def dailyTemperatures(self, temperatures):
        n=len(temperatures)
        result=[0]*n
        sta=[]
        for j in range(n):
            while sta and temperatures[j]>temperatures[sta[-1]]:
                index=sta.pop()
                result[index]=j-index
            sta.append(j)
        return result
        
        
