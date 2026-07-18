def findWays(matrix, k):
    MOD = 10**9 + 7
    n = len(matrix)
    m = len(matrix[0])  

    # we will create a 2D suffix matrix 
    # ones[i][j] will store the number of 1s from (i,j) to (n-1,m-1)
    ones = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            ones[i][j] = matrix[i][j] + ones[i+1][j] + ones[i][j+1] - ones[i+1][j+1]
    
    # if the whole matrix contains number of ones less than k, simply return 0
    if ones[0][0] < k:
        return 0
    
    # precompute the first valid cut index in O(n*m)
    next_r = [[n] * m for _ in range(n)]
    next_c = [[m] * m for _ in range(n)]  

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if i + 1 < n:
                next_r[i][j] = i + 1 if ones[i+1][j] < ones[i][j] else next_r[i+1][j]
            if j + 1 < m:
                next_c[i][j] = j + 1 if ones[i][j+1] < ones[i][j] else next_c[i][j+1]
            
    # base case : k=1 (zero cuts remaining)
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if ones[i][j] > 0:
                dp[i][j] = 1

    for step in range(2, k + 1):
        new_dp = [[0] * m for _ in range(n)]

        col_sum = [[0] * (m + 1) for _ in range(n + 1)]
        row_sum = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                col_sum[i][j] = (dp[i][j] + col_sum[i+1][j]) % MOD
                row_sum[i][j] = (dp[i][j] + row_sum[i][j+1]) % MOD
        
        # Fix 3: Indentation fixed. Yeh loop upar wale loop ke parallel hona chahiye
        # Current DP calculate 
        for i in range(n):
            for j in range(m):
                # Check if enough 1s exist to make 'step' pieces
                if ones[i][j] >= step:
                    nr = next_r[i][j]
                    nc = next_c[i][j]
                    
                    ans = 0
                    # Summing all valid horizontal cuts
                    if nr < n:
                        ans = (ans + col_sum[nr][j]) % MOD
                    
                    # Summing all valid vertical cuts
                    if nc < m:
                        ans = (ans + row_sum[i][nc]) % MOD
                        
                    new_dp[i][j] = ans
                    
        # State update (Also fixed indentation)
        dp = new_dp

    return dp[0][0]

matrix = [[1, 0, 0], [1, 1, 1], [0, 0, 0]]
k = 3 
print(findWays(matrix, k))  