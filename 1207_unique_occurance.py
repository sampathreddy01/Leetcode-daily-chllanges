from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        element_occurance=Counter(arr)
        frequency_occurance=Counter(element_occurance.values())
        for j in frequency_occurance:
            if frequency_occurance[j]>1:
                return False
        return True
        
