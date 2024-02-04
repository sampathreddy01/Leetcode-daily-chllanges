import math
class Solution(object):
    def evalRPN(self, tokens):
        sta=[]
        for j in tokens:
            if j=='+':
                a=sta.pop()+sta.pop()
                sta.append(a)
            elif j=='-':
                t=sta.pop()
                a=sta.pop()-t
                sta.append(a)
            elif j=='*':
                a=sta.pop()*sta.pop()
                sta.append(a)
            elif j=='/':
                t=sta.pop()
                a=int(float(sta.pop())/t)
                # if a<0:
                #     a+=1
                sta.append(a)
            else:
                sta.append(int(j))
        return sta.pop()
        
