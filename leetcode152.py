class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        for num in nums:
            if num == 0:
                curMin, curMax = 1, 1
                continue
            curMin, curMax = min(num, curMin*num, curMax*num), max(num, curMin*num, curMax*num)
            res = max(res, curMax)
        return res