import bisect
from typing import List
class SparseTable:
    def __init__(self, arr, op):
        self.op = op
        self.n = len(arr)
        if self.n == 0:
            return
        
        # Precompute logs for O(1) queries
        self.lg = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.lg[i] = self.lg[i // 2] + 1
            
        # Build Sparse Table
        self.st = [list(arr)]
        j = 1
        while (1 << j) <= self.n:
            row = []
            prev = self.st[-1]
            for i in range(self.n - (1 << j) + 1):
                row.append(self.op(prev[i], prev[i + (1 << (j - 1))]))
            self.st.append(row)
            j += 1

    def query(self, l, r):
        if l > r or l < 0 or r >= self.n:
            return -float('inf') if self.op == max else float('inf')
        j = self.lg[r - l + 1]
        return self.op(self.st[j][l], self.st[j][r - (1 << j) + 1])

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n=len(s)

        total_ones=s.count('1')

        # now we will find out the contigous blocks of 0s

        L,R,W=[],[],[]

        i=0

        while i<n:

            if s[i]=='0':

                st=i
                while i<n and s[i]=='0':
                    i+=1

                en=i-1

                L.append(st)
                R.append(en)
                W.append(en-st+1)
            else:
                i+=1


        m=len(L)

        if m==0:

            # if there is no zeros then no change in the sequence

            return [total_ones]* len(queries)

        #precomputation for sparse table

        O_len=[]
        sum_W=[]

        for i in range(m-1):
            O_len.append(L[i+1]-R[i]-1) # how many 1s between two zero blocks

            sum_W.append(W[i]+W[i+1])

        st_W=SparseTable(W,max)
        st_O=SparseTable(O_len,min)
        st_sumW=SparseTable(sum_W,max)


        ans=[]

        for l,r in queries:

            # find the 0 blocks that fall under l,r

            a=bisect.bisect_left(R,l)
            b=bisect.bisect_right(L,r)-1

            # if no valid internal trade found

            if a>b or a==b:
                ans.append(total_ones)
                continue

            Z_first=R[a]-max(L[a],l)+1
            Z_last = min(R[b], r) - L[b] + 1
        
            # 1. Sabse bada zero block (M) nikalna
            max_M = max(Z_first, Z_last)
            if b >= a + 2:
                max_M = max(max_M, st_W.query(a + 1, b - 1))
                
            # 2. Max adjacent zero blocks ka sum (Option 1) nikalna
            max_Z_sum = 0
            if b == a + 1:
                max_Z_sum = Z_first + Z_last
            else:
                max_Z_sum = max(Z_first + W[a + 1], W[b - 1] + Z_last)
                if b >= a + 3:
                    max_Z_sum = max(max_Z_sum, st_sumW.query(a + 1, b - 2))
                    
            # 3. Minimum 1-block dhundna jisko sacrifice karna padega (Option 2)
            min_O = st_O.query(a, b - 1)
            
            # Max Gain in dono options me se best hoga
            gain = max(max_Z_sum, max_M - min_O)
            ans.append(total_ones + gain)
        
        return ans
