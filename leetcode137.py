from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):  # For each bit position
            count = 0
            mask = 1 << i
            for num in nums:  # Count the number of 1s in this bit position
                if num & mask:
                    count += 1
            if count % 3:  # If the count is not divisible by 3, the single number has a 1 in this position
                result |= mask
        # Convert to negative number if the highest bit is set
        if result & (1 << 31):
            result -= 1 << 32
        return result
    
# Test cases
assert Solution().singleNumber([-2,-2,1,1,4,1,4,4,-4,-2]) == 3