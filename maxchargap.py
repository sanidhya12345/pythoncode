import collections
def maxCharGap(s: str) -> int:
        # code here
        
        map=collections.defaultdict(int)
        
        maxlen=-1
        for i in range(0,len(s)):
            
            if s[i] in map:
                maxlen=max(maxlen,i-(map[s[i]]+1))
            else:
                map[s[i]]=i
        
        return maxlen

s="socks"
print(maxCharGap(s))