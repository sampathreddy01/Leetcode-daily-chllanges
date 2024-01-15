class Solution(object):
    def halvesAreAlike(self, s):
        n=len(s)
        cou=0
        vowels=['a','e','i','o','u']
        for j in range(n//2):
            if s[j].lower() in vowels:
                cou+=1
        for j in range(n//2,n):
            if s[j].lower() in vowels:
                cou-=1
        if cou==0:
            return True
        return False
