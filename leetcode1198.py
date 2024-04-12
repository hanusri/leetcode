class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        def binarySearch(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        # if len of mat is greeter than 1, then check for common elements in first two arrays
        if len(mat) > 1:
            intermideateResult = []
            for num in mat[0]:
                if binarySearch(mat[1], num) != -1:
                    intermideateResult.append(num)
            
            # if intermideateResult is empty, then return -1
            if not intermideateResult:
                return -1
            
            # check for common elements in rest of the arrays
            for i in range(2, len(mat)):
                temp = []
                for num in intermideateResult:
                    if binarySearch(mat[i], num) != -1:
                        temp.append(num)
                intermideateResult = temp
            
            # if intermideateResult is empty, then return -1
            if not intermideateResult:
                return -1
            
            return intermideateResult[0]