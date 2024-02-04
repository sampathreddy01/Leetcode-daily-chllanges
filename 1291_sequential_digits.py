class Solution(object):
    def sequentialDigits(self, low, high):
        res=[]
        for i in range(1,10):
            num=i
            for j in range(i+1,10):
                num=num*10+j
                if low<=num<=high:
                    res.append(num)
                if num>high:
                    break
        return sorted(res)
