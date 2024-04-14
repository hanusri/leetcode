class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            current = 0
            days_needed = 1
            for weight in weights:
                if current + weight > mid:
                    current = weight
                    days_needed += 1
                else:
                    current += weight
            if days_needed > days:
                left = mid + 1
            else:
                right = mid
        return left