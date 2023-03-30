from typing import List


# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, return the longest palindromic substring in s.
class Solution:
	def longestPalindrome(self, s: str) -> str:
		n = len(s)
		dp = [[False for _ in range(n)] for _ in range(n)]
		
		# base cases
		for i in range(n):
			dp[i][i] = True
			if i < n - 1 and s[i] == s[i + 1]:
				dp[i][i + 1] = True

		# fill dp table: dp[i][j] = True if dp[i+1][j-1] is True and s[i] == s[j]
		for length in range(2, n):
			for i in range(n - length):
				j = i + length
				if dp[i + 1][j - 1] and s[i] == s[j]:
					dp[i][j] = True

		# find longest palindromic substring
		start, length = 0, 0

		for i in range(n):
			for j in range(i, n):
				if dp[i][j] and j - i + 1 > length:
					start = i
					length = j - i + 1
		return s[start: start + length]


# racecar
if __name__ == "__main__":
	s = Solution()
	print(s.longestPalindrome("babad"))
