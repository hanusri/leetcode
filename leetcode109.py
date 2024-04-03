from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def findMiddle(head):
            prevPtr = None
            slowPtr = head
            fastPtr = head
            while fastPtr and fastPtr.next:
                prevPtr = slowPtr
                slowPtr = slowPtr.next
                fastPtr = fastPtr.next.next
            if prevPtr:
                prevPtr.next = None
            return slowPtr
        
        if not head:
            return None
        mid = findMiddle(head)
        node = TreeNode(mid.val)
        if head == mid:
            return node
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node