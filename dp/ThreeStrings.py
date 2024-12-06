def solve(a, b, c):
    n, m = len(a), len(b)
    
    # Initialize DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] = dp[i][j-1] + (b[j-1] == c[i+j-1])
            elif j == 0:
                dp[i][j] = dp[i-1][j] + (a[i-1] == c[i+j-1])
            else:
                dp[i][j] = max(dp[i-1][j] + (a[i-1] == c[i+j-1]), dp[i][j-1] + (b[j-1] == c[i+j-1]))
    
    # Minimum changes required
    return (n + m) - dp[n][m]

# Input and Output
t = int(input())
for _ in range(t):
    a = input()
    b = input()
    c = input()
    print(solve(a, b, c))
