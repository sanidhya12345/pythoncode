class Solution:
    def canRepresentBST(self, arr):
        # code here
        stack = []
    
        # Initialize the lower bound for right subtree elements
        lower_bound = float('-inf')
        
        for val in arr:
            # If we find a node that is smaller than the current lower bound,
            # it violates the BST property.
            if val < lower_bound:
                return False
                
            # If the current value is greater than the top of the stack,
            # it means we are entering a right subtree.
            # We pop nodes until we find the parent of this right subtree.
            while stack and val > stack[-1]:
                lower_bound = stack.pop()
                
            # Push the current value onto the stack
            stack.append(val)
            
        return True