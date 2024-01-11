class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Get the lengths of the input texts
        m, n = len(text1), len(text2)
        
        # Create a 2D array to store the length of the common subsequence
        # dp[i][j] represents the length of the common subsequence of text1[:i] and text2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Iterate through the texts to fill the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If the current characters match, extend the common subsequence
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # If the characters don't match, take the maximum length from the previous rows or columns
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # The final value in the dp array represents the length of the longest common subsequence
        return dp[m][n]
