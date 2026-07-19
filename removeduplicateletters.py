from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        mp=Counter(s)

        visited=set()

        stack=[]

        for c in s:
            mp[c]-=1

            if c in visited: continue

            while stack and stack[-1] > c and mp[stack[-1]]:
                visited.remove(stack.pop())

            stack.append(c)
            visited.add(c)

        return "".join(stack) 