from collections import deque

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BT:
    def __init__(self):
        self.root=None
        
    def insert(self,data):
        newNode=TreeNode(data)
        
        if not self.root:
            self.root=newNode
            return
        
        queue=deque([self.root])
        
        while queue:
            
            curr=queue.popleft()
            
            if not curr.left:
                curr.left=newNode
                return 
            else:
                queue.append(curr.left)
            
            if not curr.right:
                curr.right=newNode
                return 
            else:
                queue.append(curr.right)
            
    def bfs(self):
        
        if not self.root:
            return []
        
        queue=deque([self.root])
        result=[]
        while queue:
            curr=queue.popleft()
            result.append(curr.data)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return result

tree=BT()

tree.insert(1)
tree.insert(5)
tree.insert(2)
tree.insert(4)
tree.insert(13)

print(tree.bfs())
        