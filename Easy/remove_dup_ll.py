class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def remove_dup(self,head):
        curr=head
        prev=None
        visited=set()
        while curr:
            if curr.val not in visited:
                visited.add(curr.val)
                prev=curr
                curr=curr.next
            else:
                nxt=curr.next
                prev.next=nxt
                curr=prev.next
        return head





