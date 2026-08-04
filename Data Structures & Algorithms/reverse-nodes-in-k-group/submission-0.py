# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            while head:
                temp_next = head.next
                head.next = prev
                prev = head
                head = temp_next
            return prev
        catch_parts = {}
        res = []
        while head:
            temp = head
            temp_head = temp
            k_temp = k - 1                          # Fix 1: k-1 since we already have the first node
            while k_temp and temp.next:
                temp = temp.next
                k_temp = k_temp-1 
            catch_parts[temp_head] = k_temp
            temp_temp = temp.next
            temp.next = None
            head = temp_temp
        for part in catch_parts.keys():
            if catch_parts[part] == 0:
                res.append(reverse(part))
            else:
                res.append(part)
        res_head = res[0]
        temp = res_head
        while temp.next:                             # Fix 4: walk to end of first part
            temp = temp.next
        for part in res[1:]:                         # Fix 4: skip first part
            temp.next = part
            while temp.next:
                temp = temp.next
        return res_head                              # Fix 3: return head, not head.next