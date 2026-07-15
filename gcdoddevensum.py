class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        
        return math.gcd(n**2,n*(n+1))