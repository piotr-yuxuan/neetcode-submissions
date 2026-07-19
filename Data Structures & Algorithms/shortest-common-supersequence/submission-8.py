class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [["" for j in range(len(str2)+1)] for i in range(len(str1)+1)]

        for i in reversed(range(len(str1)+1)):
            for j in reversed(range(len(str2)+1)):
                value = ""
                if len(str1) == i:
                    value = len(str2)-j
                elif len(str2) == j:
                    value = len(str1)-i
                elif str1[i] == str2[j]:
                    value = 1 + dp[i+1][j+1]
                elif dp[i+1][j] < dp[i][j+1]:
                    value = 1 + dp[i+1][j]
                else:
                    value = 1 + dp[i][j+1]
                dp[i][j] = value

        result = []
        i = j = 0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                result += str1[i]
                i += 1
                j += 1
            elif dp[i][j+1] < dp[i+1][j]:
                result += str2[j]
                j += 1
            else:
                result += str1[i]
                i += 1
        
        if i == len(str1):
            result.append(str2[j:])
        if j == len(str2):
            result.append(str1[i:])

        return ''.join(result)