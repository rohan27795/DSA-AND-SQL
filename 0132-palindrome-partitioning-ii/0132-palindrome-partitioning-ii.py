class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)

    # Step 1: Precompute palindrome substrings
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):  # from end to start
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

    # Step 2: DP for minimum cuts
        dp = [0] * n
        for i in range(n):
            if is_pal[0][i]:
                dp[i] = 0
            else:
                dp[i] = min(dp[j] + 1 for j in range(i) if is_pal[j + 1][i])

        return dp[-1]




        