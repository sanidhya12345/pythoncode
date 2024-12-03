n, m, k = map(int, input().split())
l = [i for i in range(n)]
dp = [[[0 for _ in range(k + 1)] for _ in range(m)] for _ in range(n + 1)]
dp[0][0][0] = 1

for i in range(1, n + 1):
    for j in range(m):
        for p in range(k + 1):
            # if we don't include the element
            if p > 0:
                dp[i][j][p] += dp[i - 1][j][p - 1]
            
            v1 = l[i - 1] % m
            prev_index = (j - v1 + m) % m
            dp[i][j][p] += dp[i - 1][prev_index][p]

print(dp[n][0][k])
