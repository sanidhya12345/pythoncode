t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    max_ones = (n + 1) // 2
    
    if k > max_ones:
        print("NO")
    else:
        if k == 0:
            print("YES")
        else:
            result = []
            # Add k number of 1s and k number of 0s in alternating pattern
            for i in range(k):
                result.append('1')
                if len(result) < n:
                    result.append('0')
            # Fill the remaining slots with 0s
            while len(result) < n:
                result.append('0')
            print("YES")
