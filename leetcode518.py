class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] += dp[a-c]
        return dp[-1]