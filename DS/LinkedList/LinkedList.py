class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertAtend(self,data):
        new_node=Node(data)
        
        if not self.head:
            self.head=new_node
        else:
            curr=self.head;
            while curr.next:
                curr=curr.next
            curr.next=new_node
    def display(self):
        curr=self.head
        
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
    def delete(self):
        if not self.head:
            return 
        curr=self.head
        while curr.next.next:
            curr=curr.next
        curr.next=None

ll=LinkedList()
ll.insertAtend(10);
ll.insertAtend(20);
ll.insertAtend(30);
ll.display()
print(ll.countNode())
ll.delete()
ll.display()
print(ll.countNode())