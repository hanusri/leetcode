class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        # get the length of linked list
        n = 0
        p = head
        while p:
            p = p.next
            n += 1
        
        p = head
        diff = abs(n - k)
        if diff == 0:
            return head
        
        for _ in range(0,diff - 1):
            p = p.next
        
        newHead = p.next
        p.next = None
        q = newHead
        while q.next:
            q = q.next
        
        q.next = head
        return newHead
