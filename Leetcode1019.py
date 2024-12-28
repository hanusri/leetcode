# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # find the count
        curr = head
        length  = 0
        while curr:
            length += 1
            curr = curr.next
        
        answer = [0] * length
        stack = []

        curr = head
        idx = 0

        while curr:
            while stack and curr.val > stack[-1][1]:
                prevIndex, _ = stack.pop()
                answer[prevIndex] = curr.val
            
            stack.append([idx, curr.val])
            curr = curr.next
            idx += 1
        
        return answer