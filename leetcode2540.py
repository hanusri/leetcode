class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        def binarySearch(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        # check which array is larger and call bbinarySearch on larger array
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        
        for i in range(len(nums2)):
            if binarySearch(nums1, nums2[i]) != -1:
                return nums2[i]
        
        return -1