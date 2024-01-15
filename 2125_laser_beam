class Solution(object):
    def numberOfBeams(self, bank):
        result=0
        prev=0
        curr=0
        n=len(bank)
        for j in range(n):
            no_of_beam=bank[j].count('1')
            if no_of_beam==0:
                continue
            prev=curr
            curr=no_of_beam
            result+=(prev*curr)
        return result
        
