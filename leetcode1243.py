from typing import List
class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        if len(arr) <= 2:
            return arr
        
        result = arr.copy()
        to_check = set(range(1, len(arr-1)))

        while to_check:
            current = result.copy()
            next_to_check = set()

            for i in to_check:
                if current[i] < current[i-1] and current[i] < current[i+1]:
                    next_to_check.update([i, i-1,i+1])
                    result[i] += 1
                elif current[i] > current[i-1] and current[i] > current[i+1]:
                    next_to_check.update([i, i-1,i+1])
                    result[i] -= 1
            
            to_check = {i for i in next_to_check if i >= 1 and i < len(arr) - 1}
        
        return result