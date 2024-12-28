class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        i = 0
        while i < len(nums):
            nums[j] = nums[i]
            j += 1
            k = i + 1
            while k < len(nums) and nums[k] == nums[i]:
                k += 1
            i = k
        
        return j
    
