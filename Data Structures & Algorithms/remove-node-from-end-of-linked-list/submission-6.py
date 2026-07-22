# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n_l = 0 
        len_finder = head
        while len_finder:
            n_l= n_l+1
            len_finder = len_finder.next
        if n > n_l:
            return None
        k = n_l-n-1
        k_count = 0
        modifier = head
        while modifier:
            if k == -1:
                head = head.next
                return head
            if k_count == k:
                if modifier.next and  modifier.next.next:
                    modifier.next = modifier.next.next
                    return head
                else:
                    modifier.next = None
                    return head
            modifier = modifier.next
            k_count = k_count+1

                    
        