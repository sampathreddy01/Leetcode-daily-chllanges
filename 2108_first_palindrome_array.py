class Solution(object):
    def isPalindrome(self,word):
        i,j=0,len(word)-1
        while i<=j:
            if(word[i]==word[j]):
                i+=1
                j-=1
            else:
                return False
        return True



    def firstPalindrome(self, words):
        for word in words:
            if self.isPalindrome(word):
                return word
        return ""
        
