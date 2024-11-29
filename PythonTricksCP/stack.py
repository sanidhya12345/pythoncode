#program to implement stack using dequeue

from collections import deque

l=[i for i in range(5)]

stack=deque(l)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

#check whether the list is empty or not

print("yes" if len(stack)==0 else "no")

