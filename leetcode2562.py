class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        result = 0
        start = 0
        end = len(nums) - 1

        while start <= end:
            if start == end:
                result += nums[start]
                break

            stringValue = str(nums[start]) + str(nums[end])
            result += int(stringValue)
            start += 1
            end -= 1
        
        return result