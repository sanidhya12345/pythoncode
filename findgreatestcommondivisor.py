from typing import List
import math
def findGCD(nums: List[int]) -> int:
        
        return math.gcd(max(nums),min(nums))

nums=list(map(int,input().split(" ")))
print(findGCD(nums))