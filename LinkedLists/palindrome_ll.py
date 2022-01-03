def palindrome_ll(head):
    #to find midddle(slow)
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    #reverse from mid to last
    prev=None
    while slow:
        nxt=slow.next
        slow.next=prev
        prev=slow
        slow=nxt
    #check palindrome
    left=head
    right=prev
    while right:
        if left.val!=right.val:
            return False
        left=left.next
        right=right.next
    return True