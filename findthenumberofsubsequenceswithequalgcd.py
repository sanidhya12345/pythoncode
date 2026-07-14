# @sanidhya12345

import math
from functools import cache


def count_gcd_pairs(nums):
    MOD=10**9+7

    n=len(nums)

    # @cache automatically memoized our function, acting as our 3d dp array
    @cache

    def dp(index,gcd1,gcd2):

        # base case: we have processed all elements in the array

        if index==n:
            #check if both the subsequences have the same gcd

            # we also check gcd1>0 to ensure neither subsequence is empty
            if gcd1==gcd2 and gcd1>0:
                return 1
            return 0
        
        # choice 1: skip the current element entirely

        res=dp(index+1,gcd1,gcd2)


        # choice 2: include the current element in subsequence 1

        new_gcd1=math.gcd(nums[index],gcd1)

        res=(res+ dp(index+1, new_gcd1,gcd2)) % MOD

        # choice 3: inclue the current element in subsequence 2

        new_gcd2=math.gcd(nums[index],gcd2)

        res=(res+ dp(index+1, gcd1,new_gcd2)) % MOD

        return res
    

    result=dp(0,0,0)
    dp.cache_clear()

    return result

nums=[1,2,3,4]
print(count_gcd_pairs(nums))