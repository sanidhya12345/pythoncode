import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n=len(nums)
        pref_gcd=[0]*n
        pref_gcd[0]=nums[0]
        pref=[0]*n
        pref[0]=nums[0]
        for i in range(1,n):
            pref[i]=max(pref[i-1],nums[i])
            pref_gcd[i]=math.gcd(nums[i],pref[i])
        pref_gcd.sort()

        start=0
        end=n-1
        sum_gcd=0

        print(pref_gcd)
        while start<end:
            sum_gcd+=math.gcd(pref_gcd[start],pref_gcd[end])
            start+=1
            end-=1
        
        return sum_gcd


