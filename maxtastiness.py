def maximumTastiness(self, prices, k):
            def canPick(mid):
                count = 1
                last_picked = prices[0]
                for i in range(1, len(prices)):
                    if prices[i] - last_picked >= mid:
                        count += 1
                        last_picked = prices[i]
                        if count == k:
                            return True
                return False

            prices.sort()
            left, right = 0, prices[-1] - prices[0]

            while left < right:
                mid = (left + right + 1) // 2
                if canPick(mid):
                    left = mid
                else:
                    right = mid - 1

            return left

prices=[13,5,1,8,21,2] 
k = 3
print(maximumTastiness(prices,k))