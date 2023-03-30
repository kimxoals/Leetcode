from typing import List

'''
https://leetcode.com/problems/generate-parentheses/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
  Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]
  Constraints:
1 <= n <= 8
'''


class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		dp = [{'()' * i} for i in range(n + 1)]
		for i in range(1, n + 1):
			for s in dp[i - 1]:
				for j in range(len(s)):
					dp[i].add(s[:j] + '()' + s[j:])
		print(dp)
		return list(dp[n])

	def generateParenthesis2(self, n: int) -> List[str]:
		def dfs(left, right, s):
			if len(s) == n * 2:
				res.append(s)
				return

			if left < n:
				dfs(left + 1, right, s + '(')

			if right < left:
				dfs(left, right + 1, s + ')')

		res = []
		dfs(0, 0, '')
		return res

	def generateParenthesis3(self, n: int) -> List[str]:
		result = []
		left = right = 0
		q = [(left, right, '')]
		while q:
			left, right, s = q.pop()
			if len(s) == 2 * n:
				result.append(s)
			if left < n:
				q.append((left + 1, right, s + '('))
			if right < left:
				q.append((left, right + 1, s + ')'))
		return result


if __name__ == "__main__":
	s = Solution()
	print(s.generateParenthesis2(2))
