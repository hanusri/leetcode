""" Or we can do the following

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n+1) // 2
        return total - sum(nums)\
     """
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
    