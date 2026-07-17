from typing import List
import bisect


class Solution:

    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        
        max_val=max(nums)

        # Step 1 : Count the frequencies of each number in nums

        freq=[0] * (max_val + 1)
        for num in nums:
            freq[num]+=1
        
        gcd_pairs_count=[0] * (max_val + 1)
        # step 2: traverse backwards from maxval to 1

        for g in range(max_val,-1,-1):

            # Count how many multiples of 'g' exist in the array

            multiple_count=0
            for m in range(g,max_val+1,g):
                multiple_count+=freq[m]

            
            # total pairs we can form using these multiples 

            pairs= multiple_count * (multiple_count-1) //2 

            for m in range(2 * g, max_val + 1, g):
                pairs-=gcd_pairs_count[m]

            gcd_pairs_count[g]=pairs


        prefix_sum=[0]*(max_val+1)
        for i in range(1,max_val + 1):
            prefix_sum[i]=prefix_sum[i-1]+gcd_pairs_count[i]
        

        answer=[]
        for q in queries:

            idx=bisect.bisect_right(prefix_sum,q)
            answer.append(idx)
        return answer