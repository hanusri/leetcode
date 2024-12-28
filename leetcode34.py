class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, first):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    if first:
                        if mid == 0 or nums[mid - 1] < target:
                            return mid
                        high = mid - 1
                    else:
                        if mid == len(nums) - 1 or nums[mid + 1] > target:
                            return mid
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        first = binary_search(nums, target, True)
        if first == -1:
            return [-1, -1]
        last = binary_search(nums, target, False)
        return [first, last]