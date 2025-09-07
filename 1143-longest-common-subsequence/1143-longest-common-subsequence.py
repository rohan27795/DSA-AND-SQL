class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m = len(text1)  # row
        n = len(text2)  # column

        if m == 0 or n == 0:
            return 0

    # Initialize DP table with (m+1) x (n+1) zeros
        t = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if text1[i - 1] == text2[j - 1]:
                    t[i][j] = 1 + t[i - 1][j - 1]
                else:
                    t[i][j] = max(t[i - 1][j], t[i][j - 1])

        return t[m][n]

        

        
        

        