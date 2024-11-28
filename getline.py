s = input()
ans = ""
for char in s:
    if char == '\\':
        break
    ans += char
print(ans)
