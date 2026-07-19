class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [["" for j in range(len(str2)+1)] for i in range(len(str1)+1)]

        for i in reversed(range(len(str1)+1)):
            for j in reversed(range(len(str2)+1)):
                value = ""
                if len(str1) == i:
                    value = str2[j:]
                elif len(str2) == j:
                    value = str1[i:]
                elif str1[i] == str2[j]:
                    value = str1[i] + dp[i+1][j+1]
                elif len(dp[i+1][j]) < len(dp[i][j+1]):
                    value = str1[i] + dp[i+1][j]
                else:
                    value = str2[j] + dp[i][j+1]
                dp[i][j] = value
                #print(f"{i=}, {j=}, [i][j]={value}")

        #print('\n'.join([' '.join([col for col in row]) for row in dp]))
        return dp[0][0]