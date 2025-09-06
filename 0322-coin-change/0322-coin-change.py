class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)
    
        t = [[float("inf")] * (amount + 1) for _ in range(n + 1)]

    
        for i in range(n + 1):
            t[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                
                    t[i][j] = min(1 + t[i][j - coins[i - 1]], t[i - 1][j])
                else:
                    t[i][j] = t[i - 1][j]

    
        return -1 if t[n][amount] == float("inf") else t[n][amount]











                 



