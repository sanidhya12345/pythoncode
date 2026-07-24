from typing import List
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique = list(set(nums))
        n = len(unique)
        
        if n == 0:
            return 0
            
        # Maximum possible XOR nikalna
        max_val = max(unique)
        max_limit = (1 << max_val.bit_length()) - 1 
        max_possible_count = max_limit + 1 
        
        # Step 2: 2 elements ka XOR
        xor2 = set()
        for i in range(n):
            for j in range(i, n):
                xor2.add(unique[i] ^ unique[j])
                
        # Step 3: 3rd element ke saath XOR with EARLY EXIT
        ans = set()
        for x in xor2:
            for c in unique:
                ans.add(x ^ c)
                
                # EARLY EXIT
                if len(ans) == max_possible_count:
                    return len(ans)
                    
        return len(ans)