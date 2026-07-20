class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        counter = 0
        revhead = None
        while head != None:
            curr_next = head.next
            if counter == 0:
                revhead = head
                revhead.next = None
            else:
                past = revhead
                revhead = head
                revhead.next = past
            head = curr_next
            counter += 1
        return revhead