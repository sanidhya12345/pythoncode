import re
s = input()
words = re.findall(r'\b[a-zA-Z]+\b', s)
print(len(words))
