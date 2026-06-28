from typing import List
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        muls=[i*k for i in range(1,105)]
        ans=-1
        for i in muls:
            if i not in nums:
                ans=i
                break
        return ans

print(Solution().missingMultiple([8,2,3,4,6],2))