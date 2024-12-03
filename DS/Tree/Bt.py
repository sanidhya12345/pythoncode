from collections import deque
# Create a Node structure
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None
    
    def insert(self,value):
        
        newNode=TreeNode(value)
        
        if not self.root:
            self.root=newNode
            return 
        #use queue to perform level order traversal
        
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
    
    #level order traversal to print the tree
    def bfs(self):
        if not self.root:
            return []
        
        result=[]
        queue=deque([self.root])
        while queue:
            curr=queue.popleft()
            result.append(curr.data)
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return result
    
    def preorder(self,root):
        if not root:
            return 
        print(root.data,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    
    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
    
    def postorder(self,root):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end=" ")
    
tree=BinaryTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)                     
tree.insert(40)
tree.insert(50)

print(tree.bfs())
print(tree.preorder(tree.root)) #10 20 40 50 30
print(tree.inorder(tree.root)) #40 20 50 10 30
print(tree.postorder(tree.root)) #40 50 20 30 10