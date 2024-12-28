class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:  # Left half is sorted
                if nums[low] <= target < nums[mid]:  # Target is in the left half
                    high = mid - 1
                else:  # Target is in the right half
                    low = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[high]:  # Target is in the right half
                    low = mid + 1
                else:  # Target is in the left half
                    high = mid - 1

        return -1  # Target is not found