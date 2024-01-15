from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):
        if (len(word1)!=len(word2)):
            return False
        count1,count2=Counter(word1),Counter(word2)
        if set(count1.keys())!=set(count2.keys()):
            return False
        freq_count1,freq_count2=Counter(count1.values()),Counter(count2.values())
        return freq_count1==freq_count2
        
