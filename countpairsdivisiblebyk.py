class Solution:
    def countKdivPairs(self, arr, k):
        # code here
        
        mp={i:0 for i in range(k)}

        count=0
        for i in arr:
            g=k-(i%k)
            g=g%k
            count+=mp[g]
            mp[i%k]+=1
        return count
            