s = input()
target = "hello"
j = 0
for char in s:
    if char == target[j]:
        j += 1
    if j == len(target):
        print("YES")
        break
else:
    print("NO")