class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertNode(self,data):
        newNode=Node(data)
        if not self.head:
            self.head=newNode
        else:
            curr=self.head
            while curr.next:
              curr=curr.next
            curr.next=newNode
    def display(self):
        curr=self.head;
        while curr:
            print(curr.data,end="->")
            curr=curr.next
        print("null")
    def countNode(self):
        curr=self.head
        count=0
        while curr:
            count+=1
            curr=curr.next
        return count
    def searchNode(self,data):
        curr=self.head
        while curr:
            if curr.data==data:
                return True
            curr=curr.next
        return False
                
ll=LinkedList()
ll.insertNode(10)
ll.insertNode(20)
ll.insertNode(30)
ll.insertNode(40)
ll.display()
print(ll.countNode())
print(ll.searchNode(30))
print(ll.searchNode(50))