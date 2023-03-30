from typing import List

'''
https://leetcode.com/problems/unique-binary-search-trees/

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
  Example 1:
Input: n = 3
Output: 5
Example 2:
Input: n = 1
Output: 1
  Constraints:
1 <= n <= 19
'''


class Solution:
	# DP
	# @cache
	def numTrees(self, n: int) -> int:
		res = 0
		if n <= 1:
			return 1
		for i in range(1, n + 1):
			res += self.numTrees(i - 1) * self.numTrees(n - i)
		return res

	# Memoization
	m = {0: 1, 1: 1}

	def numTrees2(self, n: int) -> int:
		if n in self.m:
			return self.m[n]
		self.m[n] = 0
		for i in range(1, n + 1):
			self.m[n] += self.numTrees2(i - 1) * self.numTrees2(n - i)
		return self.m[n]


if __name__ == "__main__":
	s = Solution()
	print(s.numTrees2(3))
