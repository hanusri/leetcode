from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        oddHead = ListNode(-1)
        evenHead = ListNode(-1)
        oddHeadTraverse = oddHead
        evenHeadTraverse = evenHead
        p = head
        i = 1
        while p:
            if i % 2 == 0:
                evenHeadTraverse.next = p
                evenHeadTraverse = evenHeadTraverse.next
            else:
                oddHeadTraverse.next = p
                oddHeadTraverse = oddHeadTraverse.next
            p = p.next
            i += 1
        evenHeadTraverse.next = None
        oddHeadTraverse.next = evenHead.next
        return oddHead.next
                
