class TrieNode:

    def __init__(self):
        self.children={}
        self.count=0


class Solution:
    def findPrefixes(self, arr):

        root=TrieNode()

        for word in arr:
            curr=root

            for char in word:
                if char not in curr.children:
                    curr.children[char]=TrieNode()

                curr=curr.children[char]
                curr.count+=1
        ans=[]

        for word in arr:
            curr=root
            prefix=""
            for char in word:
                prefix+=char

                curr=curr.children[char]

                if curr.count==1:
                    break
            ans.append(prefix)

        return ans

if __name__ == "__main__":
    sol = Solution()
    arr1 = ["zebra", "dog", "duck", "dove"]
    print(sol.findPrefixes(arr1)) 
    # Output: ['z', 'dog', 'du', 'dov']
    
    arr2 = ["geeksgeeks", "geeksquiz", "geeksforgeeks"]
    print(sol.findPrefixes(arr2)) 
    # Output: ['geeksg', 'geeksq', 'geeksf']