class Solution(object):
    def groupAnagrams(self, strs):
        l={}
        for word in strs:
            sorted_word=''.join(sorted(word))
            if sorted_word in l:
                l[sorted_word].append(word)
            else:
                l[sorted_word]=[word]
        res=[]
        for j in l:
            res.append(l[j])
        return res
