import math
from typing import List

'''
https://leetcode.com/problems/counting-bits/

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
  Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
6 --> 110
7 --> 111
8 --> 1000
9 --> 1001
  Constraints:
0 <= n <= 105
  Follow up:
It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

'''


class Solution:
	# First try
	def countBits(self, n: int) -> List[int]:
		res = [0]
		for i in range(1, n + 1):
			if (i & (i - 1) == 0) and i != 0:
				res.append(1)
			elif i % 2 == 0:
				max = pow(2, i.bit_length() - 1)
				res.append(res[max] + res[i - max])
			else:
				res.append(res[i - 1] + 1)
			print(i, bin(i), res[i])
		return res

	# Simplified sol 1
	def countBits2(self, n: int) -> List[int]:
		res = [0 for _ in range(n + 1)]
		diff = 1
		for i in range(1, n + 1):
			if diff * 2 == i:
				diff *= 2
			res[i] = res[i - diff] + 1
		return res

	def solve(self, n, m):
		if n == 0:
			return 0

		if m[n] >= 1:
			return m[n]

		if n % 2 == 0:
			return self.solve(n // 2, m)
		else:
			return self.solve(n // 2, m) + 1

	# DP
	def countBits3(self, n: int) -> List[int]:
		m = [0 for _ in range(n + 1)]
		for i in range(n + 1):
			m[i] = self.solve(i, m)
		return m


if __name__ == "__main__":
	s = Solution()
	print(s.countBits3(16))
	print([0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1])
