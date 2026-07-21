class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        n = len(t)

        left_zero = [0] * n
        right_zero = [0] * n

        for i in range(n):
            if t[i] == '0':
                left_zero[i] = (left_zero[i-1] if i > 0 else 0) + 1

        for i in range(n - 1, -1, -1):
            if t[i] == '0':
                right_zero[i] = (right_zero[i+1] if i < n-1 else 0) + 1

        total_ones = s.count('1')
        max_gain = 0

        i = 1
        while i < n - 1:
            if t[i] == '1':
                j = i
                while j < n - 1 and t[j] == '1':
                    j += 1
                # '1'-block from i to j-1, check left/right zero runs
                if t[i-1] == '0' and t[j] == '0':
                    gain = left_zero[i-1] + right_zero[j]
                    max_gain = max(max_gain, gain)
                i = j
            else:
                i += 1

        return total_ones + max_gain