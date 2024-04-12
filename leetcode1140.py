class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        # number of stones that alice gets
        def dfs(alice, i, M):
            if i == len(piles):
                return 0
            if dp.get((i, M, alice)) is not None:
                return dp[(i, M, alice)]
            res = 0 if alice else float('inf') # if alice, maximize, else minimize
            total = 0
            for X in range(1, 2*M+1):
                if i+X > len(piles):
                    break
                total += piles[i+X-1]
                if alice:
                    res = max(res, total + dfs(not alice, i+X, max(M, X)))
                else:
                    res = min(res, dfs(not alice, i+X, max(M, X)))
            dp[(i, M, alice)] = res
            return res
        
        return dfs(True, 0, 1)
            