def myAtoi(self, s):
        # Code here
        d = s.strip()
sign = 1
start_index = 0
if d[0] == '-':
    sign = -1
    start_index = 1
elif d[0] == '+':
    start_index = 1

con = ""
for i in range(start_index, len(d)):
    if d[i].isdigit():
        con += d[i]
    else:
        break

if con == "":
    print(0)
    exit()

ans = sign * int(con)

INT_MIN = -2147483648
INT_MAX = 2147483647

if ans < INT_MIN:
    print(INT_MIN)
elif ans > INT_MAX:
    print(INT_MAX)
else:
    print(ans)
