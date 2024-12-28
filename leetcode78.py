from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, path):
            res.append(path)
            for i in range(start, len(nums)):
                backtrack(i+1, path+[nums[i]])
        backtrack(0, [])
        return res

# Test this code
nums = [1, 2]
sol = Solution()
print(sol.subsets(nums))
        