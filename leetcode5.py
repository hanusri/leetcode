class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        longest = ""
        for i in range(len(s)):
            # Find longest odd length palindrome with s[i] at its center
            odd_len_palindrome = expand_around_center(i, i)
            if len(odd_len_palindrome) > len(longest):
                longest = odd_len_palindrome
            
            # Find longest even length palindrome with s[i] and s[i+1] at its center
            even_len_palindrome = expand_around_center(i, i+1)
            if len(even_len_palindrome) > len(longest):
                longest = even_len_palindrome
        
        return longest