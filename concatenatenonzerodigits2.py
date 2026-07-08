from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        m = len(s)
        
        # Precompute powers of 10 modulo MOD to quickly shift digits
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        sum_digits = [0] * (m + 1)
        pos = [0] * (m + 1)
        nz_val = [0]
        
        current_nz_val = 0
        nz_idx = 0
        
        # Build prefix arrays in a single O(N) pass
        for i in range(m):
            d = int(s[i])
            
            # Prefix sum of all digits
            sum_digits[i + 1] = sum_digits[i] + d
            
            # Record how many non-zero digits we've seen BEFORE index i
            pos[i] = nz_idx 
            
            if d != 0:
                # Update the running value of our non-zero integer
                current_nz_val = (current_nz_val * 10 + d) % MOD
                nz_val.append(current_nz_val)
                nz_idx += 1
                
        # Record the boundary for the end of the string
        pos[m] = nz_idx
        
        ans = []
        for l, r in queries:
            # 1. Get the sum of digits in O(1)
            s_d = sum_digits[r + 1] - sum_digits[l]
            
            # 2. Map original string indices to our non-zero array indices
            L = pos[l]
            R_plus_1 = pos[r + 1]
            
            if L == R_plus_1:
                # If L == R_plus_1, there were no non-zero digits in this range
                ans.append(0)
            else:
                # Extract the integer value using modular arithmetic
                length = R_plus_1 - L
                x = (nz_val[R_plus_1] - nz_val[L] * pow10[length]) % MOD
                
                # Append the final answer for this query
                ans.append((x * s_d) % MOD)
                
        return ans