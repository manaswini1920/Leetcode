class LinkedList:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next = next
class Solution:
    def mid_of_ll(self,head):
        head=LinkedList()
        node=start=head
        length=0
        while start:
            length+=1
            start=start.next

        mid=length//2
        count=0
        while node:
            if count==mid:
                return node
            else:
                count+=1
                node=node.next
        return None


s=Solution()
s.mid_of_ll([1,2,3,4,5])

'''
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
'''