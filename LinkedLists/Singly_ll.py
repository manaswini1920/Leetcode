class Node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
class Single_linkedlist:
    def __init__(self):
        self.head=Node(0)
        self.size=0
    def add_at_index(self,index,val):#we will check for prev and attach prev with new
        #base case
        if index<0:
            index=0 #insert at head
        if index>self.size:
            return
        self.size+=1
        #find prev
        prev=self.head
        for _ in range(index):
            prev=prev.next
        #create new node
        new_node=Node(val)
        #insert
        new_node.next=prev.next
        prev.next=new_node
    def add_at_beg(self,val):
        self.add_at_index(0,val)
    def add_at_end(self,val):
        self.add_at_index(self.size,val)
    def get(self,index):
        #base case
        if index<0 or index>=self.size:
            return -1
        curr=self.head
        for _ in range(index+1):
            curr=curr.next
        return curr.val
    def delete_at_index(self,index):
        #base case
        if index<0 or index>self.size:
            return
        self.size-=1
        #find prev
        prev=self.head
        for _ in range(index):
            prev=prev.next
        #attach prev to curr.next
        prev.next=prev.next.next
l=Single_linkedlist()
l.add_at_index(0,1)
l.add_at_end(2)

print(l.get(1))
