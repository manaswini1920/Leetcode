def insert_into_cyclic_sorted_ll(head,insertval):
    newnode=Node(0)
    if not head:
        newnode.next=newnode
        return newnode
    prev=head #tail
    curr=head.next
    while prev.next!=head:
        #case 1 insert between
        if prev.val<=insertval<=curr.val:
            break
        #case 2 less than head and greater than tail
        if prev.val>curr.val and (insertval>prev.val or insertval<curr.val):
            break
        #iterate
        prev=prev.next
        curr=curr.next
    #insert
    newnode.next=curr
    prev.next=newnode
    return head

