class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        total = sum(nums) // 2
        dp = set()
        dp.add(0)
        for num in nums:
            new_dp = set()
            for i in dp:
                new_dp.add(i + num)
                if i + num == total:
                    return True
            dp = dp.union(new_dp)
        return False