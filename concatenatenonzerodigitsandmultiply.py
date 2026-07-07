class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=str(n)
        num=""
        sm=0
        for i in range(0,len(s)):
            if s[i]!='0':
                num+=s[i]
                sm+=int(s[i])
        if sm==0:
            return 0
        return sm*int(num)