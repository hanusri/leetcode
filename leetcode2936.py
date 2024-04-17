from typing import Optional
# Definition for BigArray.
# class BigArray:
#     def at(self, index: long) -> int:
#         pass
#     def size(self) -> long:
#         pass
class Solution(object):
    def countBlocks(self, nums: Optional['BigArray']) -> int:
        out = 0
        indx = 0
        prev = curr = None
        n = nums.size()

        def getNextIndex(start, target):
            left, right = start, n-1            
            while left <= right:
                mid = right - (right-left) // 2
                curr = nums.at(mid)
                if curr != target:
                    right = mid-1
                else:
                    left = mid+1            
            return right

        while indx < n:
            curr = nums.at(indx)
            nxt = getNextIndex(indx, curr)
            indx = nxt+1
            out += 1

        return out