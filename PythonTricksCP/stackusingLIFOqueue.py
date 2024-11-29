from queue import LifoQueue

stack=LifoQueue(maxsize=5)

for i in range(5):
    stack.put(i)
    
print(stack.full()) #check whether the stack is full or not
print(stack.empty()) #check whether the stack is empty or not


#pop out the element from the stack

print(stack.get())
print(stack.get())
print(stack.get())