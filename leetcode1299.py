from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if arr is None or len(arr) < 1:
            return arr
        
        result = [-1 for i in range(0, len(arr))]

        calculation_list = [0]
        for i in range(1, len(arr)):
            while calculation_list and arr[calculation_list[-1]] < arr[i]:
                result[calculation_list.pop()] = arr[i]
            calculation_list.append(i)
        
        return result