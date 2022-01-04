def flatten_dll(head):
    dummy=Node(0)
    curr= dummy
    stack=[head]
    while stack:
        top=stack.pop()
        if top.next:
            stack.append(top.next)
        if top.child:
            stack.append(top.child)
        curr.next=top
        top.prev=curr
        top.child=None
        curr=curr.next
    dummy.next.prev=None
    return dummy.next