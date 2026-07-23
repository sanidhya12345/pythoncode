from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Base cases for n=1 and n=2
        if n <= 2:
            return n
            
        # For n >= 3, the number of unique XOR triplets is 2^(bit_length of n)
        # 1 << m is equivalent to 2^m
        return 1 << n.bit_length()