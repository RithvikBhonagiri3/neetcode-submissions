class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        linked_list_elements = set()
        while head:
            curr_next = head.next
            if head in linked_list_elements:
                break
            else:
                linked_list_elements.add(head)
            head = curr_next
        if head:
            res = True
        else:
            res = False
        return res