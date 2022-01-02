class LinkedList:
    def hascycle(self,head):
        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False