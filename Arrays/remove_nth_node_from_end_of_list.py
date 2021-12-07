def remove_nth_from_end(head,n):
    fast=slow=head
    for _ in range(n):
        fast=fast.next
    if not fast:
        return head.next
    #fast stops at nth node
    while fast.next:
        fast=fast.next
        slow=slow.next
    #slow will be at prev of nth node which should connect to next of nth node
    slow.next=slow.next.next
    return head
