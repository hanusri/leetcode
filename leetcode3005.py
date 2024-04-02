class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Count the frequency of each number
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Find the maximum frequency
        max_freq = max(freq.values())

        # Count how many numbers have the maximum frequency
        count = sum(value for value in freq.values() if value == max_freq)

        return count