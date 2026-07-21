# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        real_input_head = head
        rev_head = None
        original_dummy = ListNode()
        original = original_dummy
        originaln_dummy = ListNode()
        originaln = originaln_dummy
        while head:
            original.next = ListNode(head.val)
            originaln.next = ListNode(head.val)
            head = head.next
            original = original.next
            originaln = originaln.next
        original = original_dummy.next
        head = originaln_dummy.next
        while head:
            curr_next = head.next
            head.next = rev_head
            rev_head = head
            head = curr_next
        dummy_res = ListNode()
        res = dummy_res
        head = original
        while head and rev_head and head !=rev_head:
            curr_head_nxt = head.next
            curr_rev_head_nxt = rev_head.next
            res.next = head
            res = res.next
            res.next = rev_head
            res = res.next
            head = curr_head_nxt
            rev_head = curr_rev_head_nxt
        # FIXED: LeetCode requires modifying the original nodes in-place.
        # We overwrite the values of the original list using our perfect reordered chain.
        mover = real_input_head
        final_chain = dummy_res.next
        while mover:
            mover.val = final_chain.val
            mover = mover.next
            final_chain = final_chain.next
        return mover