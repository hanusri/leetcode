class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand_around_center(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        
        total = 0
        for i in range(len(s)):
            # Count odd length palindromes with s[i] at its center
            total += expand_around_center(i, i)
            
            # Count even length palindromes with s[i] and s[i+1] at its center
            total += expand_around_center(i, i+1)
        
        return total