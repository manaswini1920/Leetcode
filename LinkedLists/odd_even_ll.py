def odd_even(head):
    if not head:
        return None
    odd=head
    even=head.next
    evenhead=even
    while even and even.next:
        odd.next=even.next
        odd=odd.next
        even.next=odd.next
        even=even.next
    odd.next=evenhead
    return head