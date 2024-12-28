class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # Remove leading whitespaces
        if not s: return 0  # Return 0 if string is empty

        # Check for sign
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            sign = 1

        # Convert string to integer
        i = 0
        while i < len(s) and s[i].isdigit():
            i += 1
        num = s[:i]
        if not num: return 0  # Return 0 if no digits were read

        # Apply sign and round to 32-bit signed integer range
        num = sign * int(num)
        num = max(min(num, 2**31 - 1), -2**31)

        return num