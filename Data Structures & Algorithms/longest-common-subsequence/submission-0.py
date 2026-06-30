class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]

        for i in range(len(text1)):
            for j in range(len(text2)):

                if text1[i] == text2[j]:
                    prior_ij = dp[i-1][j-1] if (0 <= j-1 and 0 <= j-1) else 0
                    dp[i][j] = 1 + prior_ij
                else:
                    prior_i = dp[i-1][j] if 0 <= i-1 else 0
                    prior_j = dp[i][j-1] if 0 <= j-1 else 0

                    dp[i][j] = max(prior_i, prior_j)
        return dp[-1][-1]
