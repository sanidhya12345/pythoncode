from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if nums==[k]*len(nums):
            return 0
        
        s=set()
        for i in nums:
            if i>k and i not in s:
                s.add(i)
        
        if len(s)!=0 and min(s)>=k:
            return len(s)
        return -1       
        
l=[5,2,5,4,5]
k=2
ans=Solution()
print(ans.minOperations(l,k))