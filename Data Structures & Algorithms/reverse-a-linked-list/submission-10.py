# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        revhead = None
        while head:
            curr_next = head.next
            head.next = revhead
            revhead = head
            head = curr_next
        return revhead

        