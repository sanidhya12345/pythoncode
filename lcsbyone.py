from collections import defaultdict

class Solution:
    def waysToIncreaseLCSBy1(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        
        # 1. Prefix LCS DP (lcsl[i][j] = LCS of s1[0..i-1] and s2[0..j-1])
        lcsl = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    lcsl[i][j] = lcsl[i - 1][j - 1] + 1
                else:
                    lcsl[i][j] = max(lcsl[i - 1][j], lcsl[i][j - 1])
                    
        # 2. Suffix LCS DP (lcsr[i][j] = LCS of s1[i..n1-1] and s2[j..n2-1])
        lcsr = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                if s1[i] == s2[j]:
                    lcsr[i][j] = lcsr[i + 1][j + 1] + 1
                else:
                    lcsr[i][j] = max(lcsr[i + 1][j], lcsr[i][j + 1])
                    
        # 3. Store the positions of every character in s2 for fast lookup
        pos = defaultdict(list)
        for j, char in enumerate(s2):
            pos[char].append(j)
            
        base_lcs = lcsl[n1][n2]
        ways = 0
        
        # 4. Test all possible insertion points (i) and all characters (a-z)
        for i in range(n1 + 1):
            for char_code in range(97, 123):  # ASCII 'a' to 'z'
                ch = chr(char_code)
                
                # We want to see if 'ch' matches with some s2[j] such that it forms a bridge
                # making the new LCS = base_lcs + 1. We just need to find ONE valid j to count it.
                for j in pos[ch]:
                    if lcsl[i][j] + lcsr[i][j + 1] == base_lcs:
                        ways += 1
                        break  # We only count this (position, character) combo once!
                        
        return ways