class LinkedList:
    def detect_start_point(self,head):

        def intersect_point(head):
            fast = slow = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return fast
            return None
        if head is None:
            return None
        s1=intersect_point(head)
        if s1 is None:
            return None
        s2=head
        while s1!=s2:
            s1=s1.next
            s2=s2.next
        return s1