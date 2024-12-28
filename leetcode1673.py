from typing import List
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for i, item in enumerate(nums):
            while ans and ans[-1] < item and k - len(ans) <= len(nums) - 1 - i:
                ans.pop()
            
            if len(ans) < k:
                ans.append(item)
        return ans