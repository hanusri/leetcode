class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Determine the sign of the result
        sign = -1 if ((dividend < 0) ^  (divisor < 0)) else 1
        
        # Convert both numbers to positive
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0
        while dividend >= divisor:
            temp = divisor
            i = 1
            while dividend >= temp:
                dividend -= temp
                result += i
                i <<= 1
                temp <<= 1
        
        # Apply the sign and return the result
        result *= sign
        
        # Handle overflow
        if result < -2**31:
            return -2**31
        if result > 2**31 - 1:
            return 2**31 - 1
        return result
    
# Test cases
solution = Solution()
assert solution.divide(50, 6) == 8