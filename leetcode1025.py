class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False for _ in range(n+1)]
        
        for i in range(2, n+1):
            for x in range(1, i):
                if i % x == 0 and not dp[i - x]:
                    dp[i] = True
                    break
                    
        return dp[n]