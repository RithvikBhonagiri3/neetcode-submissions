# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res_pre = ListNode(-1001)
        res_move = res_pre
        counter = 0
        for ele in lists:
            if not ele:
                continue
            else:
                if counter == 0:
                    res_move.next = ele
                    res_move = res_move.next
                    ele_mover = ele.next
                    counter = counter+1
                    while ele_mover:
                        res_move = res_move.next
                        ele_mover = ele_mover.next
                    continue
                else:
                    ele_mover = ele
                    comp_start = res_pre.next
                    while ele_mover:
                        while comp_start:
                            if not ele_mover:
                                break
                            if ele_mover.val >= comp_start.val and not comp_start.next:
                                while ele_mover:
                                    comp_start.next = ele_mover
                                    comp_start = comp_start.next
                                    ele_mover = ele_mover.next

                            elif ele_mover.val >=comp_start.val and ele_mover.val < comp_start.next.val:
                                temp_holder_comp = comp_start.next
                                temp_holder_ele_mover = ele_mover.next
                                comp_start.next = ele_mover
                                comp_start = comp_start.next
                                comp_start.next = temp_holder_comp
                                ele_mover = temp_holder_ele_mover
                            elif ele_mover.val < comp_start.val:
                                # Fix 1: find the node pointing to comp_start and update its next
                                temp_holder_ele_mover = ele_mover.next
                                ele_mover.next = comp_start
                                #comp_start = ele_mover
                                # walk res_pre to find parent of comp_start
                                parent = res_pre
                                while parent.next != comp_start:
                                    parent = parent.next
                                parent.next = ele_mover
                                ele_mover = temp_holder_ele_mover
                            else:
                                comp_start = comp_start.next
                        

        return res_pre.next



        

        