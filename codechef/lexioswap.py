class Pair:
    def __init__(self, char, count):
        self.char = char
        self.count = count

def solve(n, m, s, t):
    s_pair = []
    t_pair = []
    stopchar = 's'
    count = 0

    # Process the first string
    for i in range(0, n):
        if stopchar == s[i]:
            count += 1
        else:
            if stopchar != 's':
                s_pair.append(Pair(stopchar, count + 1))
            count = 0
            stopchar = s[i]
    s_pair.append(Pair(stopchar, count + 1))

    # Process the second string
    stopchar = 's'
    count = 0
    for i in range(0, m):
        if stopchar == t[i]:
            count += 1
        else:
            if stopchar != 's':
                t_pair.append(Pair(stopchar, count + 1))
            count = 0
            stopchar = t[i]
    t_pair.append(Pair(stopchar, count + 1))

    # Compare the pairs
    if len(s_pair) != len(t_pair):
        print("NO")
        return

    mismatch = False
    for i in range(len(s_pair)):
        if s_pair[i].char == t_pair[i].char:
            if s_pair[i].count >= t_pair[i].count:
                diff = s_pair[i].count - t_pair[i].count
                if diff % 2 != 0:
                    mismatch = True
            else:
                mismatch = True
        else:
            mismatch = True

    if len(s_pair) == 1 and len(t_pair) == 1:
        if s == t:
            print("YES")
        else:
            print("NO")
    elif mismatch:
        print("NO")
    else:
        print("YES")

# Input processing
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    t = input()
    solve(n, m, s, t)
