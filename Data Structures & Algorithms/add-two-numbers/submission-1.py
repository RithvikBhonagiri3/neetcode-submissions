# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # first reverse Linked lists
        l1rev = None
        l2rev = None
        dummy = ListNode()
        rerev = dummy
        while l1 or l2:
            rerev.next = ListNode()
            rerev = rerev.next
            if l1:
                rerev.val = rerev.val+l1.val
                l1 = l1.next
            if l2:
                rerev.val = rerev.val+l2.val
                l2 = l2.next
        next_transfer = 0
        mover = dummy.next
        while mover:
            mover.val = mover.val+next_transfer
            if mover.val/10 >=1:
                mover.val = mover.val % 10
                next_transfer = 1
            else:
                next_transfer = 0
            if next_transfer and not mover.next:
                mover.next = ListNode(0)
            mover = mover.next
        return dummy.next
            
        


        