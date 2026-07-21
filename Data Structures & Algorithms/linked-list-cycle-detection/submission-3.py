class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_tracker = head
        fast_tracker = head
        while fast_tracker and fast_tracker.next:
            slow_tracker = slow_tracker.next
            fast_tracker = fast_tracker.next.next
            if slow_tracker == fast_tracker:
                return True
        return False