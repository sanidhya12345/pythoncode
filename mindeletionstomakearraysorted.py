from bisect import bisect_left

class Solution:
    def minDeletions(self, arr):
        if not arr:
            return 0
            
        lis = []
        
        for num in arr:
            # Find the index where 'num' should be inserted in the sorted 'lis' array
            idx = bisect_left(lis, num)
            
            # If the number is greater than all elements in lis, append it
            if idx == len(lis):
                lis.append(num)
            # Otherwise, replace the element at idx to keep the sequence elements as small as possible
            else:
                lis[idx] = num
                
        # Total elements - Length of Longest Increasing Subsequence
        return len(arr) - len(lis)