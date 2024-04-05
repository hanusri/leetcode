from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Push nodes onto the stack
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next

        # Pop nodes from the stack and remove nodes
        max_node = None
        while stack:
            node = stack.pop()
            if max_node is None or node.val >= max_node.val:
                node.next = max_node
                max_node = node
            # Otherwise, the node is removed by not updating node.next

        return max_node