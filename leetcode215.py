from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = []
        for num in nums:
            if len(result) < k:
                heapq.heappush(result, num)
            else:
                heapq.heappushpop(result, num)
        
        return heapq.heappop(result)