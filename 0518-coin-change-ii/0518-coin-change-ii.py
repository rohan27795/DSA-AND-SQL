class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n = len(coins)
        t = [[0] * (amount + 1) for i in range(n + 1)]

        for i in range(n + 1):
            t[i][0] = 1 # if you want count of ways, usually this is 1 (base case)

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if coins[i-1] <= j:
                    t[i][j] = t[i][j - coins[i-1]] + t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]

        return t[n][amount]
        