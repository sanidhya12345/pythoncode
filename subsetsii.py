from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        for mask in range(1<<n):
            l=[]
            for i in range(n):
                if mask & (1<<i):
                    l.append(nums[i])
            ans.append(l)
        fans=[]
        for i in ans:
            if i not in fans:
                fans.append(i)
        return fans