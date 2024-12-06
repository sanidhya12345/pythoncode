def modified(n):
    sq = str(n ** 2)
    d = len(str(n))
    split1 = sq[:len(sq) - d] if len(sq) > d else "0"
    split2 = sq[len(sq) - d:]
    if int(split1) + int(split2) == n:
        return True
    return False

a = int(input())
b = int(input())
l = []
for i in range(a, b + 1):
    if modified(i):
        l.append(i)
if len(l)<=0:
    print("INVALID RANGE")
else:
    print(*l)
