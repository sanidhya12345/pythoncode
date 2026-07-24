'''
Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def longestConsecutive(self, root):
        if not root:
            return -1
            
        max_len = 0
        
        def dfs(node, expected_val, current_len):
            nonlocal max_len
            if not node:
                return
            
            # If the current node matches the expected value, extend the path
            if node.data == expected_val:
                current_len += 1
            else:
                # Otherwise, reset the sequence length to 1
                current_len = 1
                
            # Update the global maximum length found so far
            max_len = max(max_len, current_len)
            
            # Recurse for left and right children, expecting value + 1
            dfs(node.left, node.data + 1, current_len)
            dfs(node.right, node.data + 1, current_len)
            
        # Start the DFS. Passing root.data ensures the first match succeeds 
        # and current_len becomes 1.
        dfs(root, root.data, 0)
        
        # A valid consecutive path must have at least 2 nodes (parent to child)
        return max_len if max_len > 1 else -1