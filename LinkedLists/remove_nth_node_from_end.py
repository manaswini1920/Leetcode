class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class LinkedList:
    def remove_nth(self,head,n):
        dummy=ListNode(0)
        dummy.next=head
        fast=slow=dummy
        for _ in range(n):
            fast=fast.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.nexr.next
        return dummy.next