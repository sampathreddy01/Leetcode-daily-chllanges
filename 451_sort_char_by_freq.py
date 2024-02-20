class Solution(object):
    def frequencySort(self, s):
        ans,freq = '',defaultdict(list)
        count = Counter(s)
        maxFreq = 0

        for key,val in count.items():
            freq[val]+=[key]*val
            maxFreq = max(maxFreq,val)

        while maxFreq:
            ans+=''.join(freq[maxFreq])
            maxFreq-=1

        return ans
        
