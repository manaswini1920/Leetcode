def merge_lists(l1,l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.val<l2.val:
        l1.next=merge_lists(l1.next,l2)
        return l1
    else:
        l2.next=merge_lists(l2.next,l1)
        return l2
'''
approach 2
def merge(l1,l2):
    dummy=ListNode(0)
    curr=dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next=l1
            l1=l1.next
        else:
            curr.next=l2
            l2=l2.next
        curr=curr.next
    #left overs
    if l1:
        curr.next=l1
    if l2:
        curr.next=l2
    return dummy.next
'''