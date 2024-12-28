from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0 for _ in range(len(nums)+1)]
        dp[0] = 0
        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])
        
        for i in range(3, len(nums) + 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        
        return dp[-1]