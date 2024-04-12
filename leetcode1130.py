# reference https://www.youtube.com/watch?v=XsQnspXX8bk&t=623s
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        cache = {} # left, right

        def dp(left, right) -> (int, int): #maxValue, nonLeafSum
            if (left, right) in cache:
                return cache[(left, right)]
            
            if left == right:
                cache[(left, right)] = (arr[left], 0)
                return cache[(left, right)]
            
            res_sum = float('inf')
            res_max = float('-inf')

            for i in range(left +1, right + 1):
                left_max, left_sum = dp(left, i-1)
                right_max, right_sum = dp(i, right)
                res_max = max(res_max, left_max, right_max)
                res_sum = min(res_sum, left_sum + right_sum + left_max * right_max)
            cache[(left, right)] = (res_max, res_sum)
            return cache[(left, right)]
        
        return dp(0, len(arr)-1)[1]

