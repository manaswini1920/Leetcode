

class LinkedList:
    def __init__(self):
        pass
    def merge_k_sorted_lists(self,lists):
        if not lists or len(lists)==0:
            return None
        while len(lists)>1:
            output=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1<len(lists) else None
                output.append(self.merge_two(l1,l2))
            lists=output
        return lists[0]
    def merge_two(l1,l2):
        dummy=Node(0)
        curr=dummy
        while l1 and l2:
            if l1.val<l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.val
            curr=curr.next
        if l1:
            curr.next=l1
        if l2:
            curr.next=l2
        return dummy.next
class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
