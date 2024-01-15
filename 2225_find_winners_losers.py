class Solution(object):
    def findWinners(self, matches):
        winners=[]
        one_time_losers=[]
        result=[]
        coun={}
        for winner,loser in matches:
            if winner not in coun:
                coun[winner]=0
            if loser in coun:
                coun[loser]+=1
            else:
                coun[loser]=1
        for j in coun:
            if coun[j]==0:
                winners.append(j)
            elif coun[j]==1:
                one_time_losers.append(j)
        winners.sort()
        one_time_losers.sort()
        result.append(winners)
        result.append(one_time_losers)
        return result
            
