class Solution:
    def maxIndexDiff(self, s: str) -> int:

        min_start = [float('inf')] * 26
        
       
        max_diff = -1
        
        for i in range(len(s)):
            char_idx = ord(s[i]) - ord('a')
            
            if char_idx == 0:
                min_start[0] = min(min_start[0], i)
                max_diff = max(max_diff, 0)
                
            else:
                if min_start[char_idx - 1] != float('inf'):
                    min_start[char_idx] = min(min_start[char_idx], min_start[char_idx - 1])
                    max_diff = max(max_diff, i - min_start[char_idx])
                    
        return max_diff
