class Solution:
    def maxDiffSubArrays(self, arr):
        n = len(arr)
        if n < 2:
            return 0
            
        # Arrays to store the min/max subarray sums from left to right
        leftMax = [0] * n
        leftMin = [0] * n
        
        # Arrays to store the min/max subarray sums from right to left
        rightMax = [0] * n
        rightMin = [0] * n
        
        # 1. Fill leftMax and leftMin using Kadane's algorithm
        currMax = currMin = arr[0]
        leftMax[0] = leftMin[0] = arr[0]
        
        for i in range(1, n):
            currMax = max(arr[i], currMax + arr[i])
            leftMax[i] = max(leftMax[i-1], currMax)
            
            currMin = min(arr[i], currMin + arr[i])
            leftMin[i] = min(leftMin[i-1], currMin)
            
        # 2. Fill rightMax and rightMin using Kadane's algorithm backwards
        currMax = currMin = arr[n-1]
        rightMax[n-1] = rightMin[n-1] = arr[n-1]
        
        for i in range(n-2, -1, -1):
            currMax = max(arr[i], currMax + arr[i])
            rightMax[i] = max(rightMax[i+1], currMax)
            
            currMin = min(arr[i], currMin + arr[i])
            rightMin[i] = min(rightMin[i+1], currMin)
            
        # 3. Find the maximum absolute difference across all valid split points
        max_diff = 0
        for i in range(n - 1):
            # Difference if max is on the left and min is on the right
            diff1 = abs(leftMax[i] - rightMin[i+1])
            # Difference if min is on the left and max is on the right
            diff2 = abs(leftMin[i] - rightMax[i+1])
            
            max_diff = max(max_diff, diff1, diff2)
            
        return max_diff