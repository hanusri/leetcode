from typing import List
from collections import defaultdict
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:      
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
            if count_map[num] > 2:
                return False
        
        return True
