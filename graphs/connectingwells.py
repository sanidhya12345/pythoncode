from collections import defaultdict, deque

def solve(points):
    def checkConnectionTime(x1, y1, x2, y2):
        if y1 == y2:
            return (abs(x1 - x2) + 1) // 2 if abs(x1 - x2) % 2 != 0 else abs(x1 - x2) // 2
        elif x1 == x2:
            return (abs(y1 - y2) + 1) // 2 if abs(y1 - y2) % 2 != 0 else abs(y1 - y2) // 2
        return max(abs(x1 - x2), abs(y1 - y2))

    def isConnectedAtTime(mid):
        # Build graph for wells that can connect within time `mid`
        graph = defaultdict(list)
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if checkConnectionTime(x1, y1, x2, y2) <= mid:
                    graph[i].append(j)
                    graph[j].append(i)

        # Check if graph is fully connected using BFS or DFS
        visited = [False] * n

        def bfs(start):
            queue = deque([start])
            visited[start] = True
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

        bfs(0)  # Start BFS from the first well
        return all(visited)

    # Binary search to find the minimum time
    low, high = 0, 10**9
    answer = -1

    while low <= high:
        mid = (low + high) // 2
        if isConnectedAtTime(mid):
            answer = mid
            high = mid - 1  # Look for a smaller time
        else:
            low = mid + 1  # Increase time

    return answer

# Input handling
t = int(input())
for _ in range(t):
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    print(solve(points))
