"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        res = Node(head.val)
        mover = res
        org = head

        rand_dict = {}
        rand_dict[org] = mover
        org = org.next
        while org:
            mover.next = Node(org.val)
            mover = mover.next
            rand_dict[org] = mover
            org = org.next

        mover = res
        org = head
        while org:
            if org.random:
                mover.random = rand_dict.get(org.random)
            
            mover = mover.next
            org = org.next
        return res
