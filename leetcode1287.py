class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        quarter = n // 4
        
        for i in range(n - quarter):
            if arr[i] == arr[i + quarter]:
                return arr[i]
        
        # This return statement should never be reached given the problem constraints
        return -1