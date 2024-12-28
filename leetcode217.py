class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for i in nums:
            if i in num_set:
                return True
            num_set.add(i)
        return False
# Time complexity: O(n)
    
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict = {}
        for i, num in enumerate(nums):
            if num in num_dict and i - num_dict[num] <= k:
                return True
            num_dict[num] = i
        return False