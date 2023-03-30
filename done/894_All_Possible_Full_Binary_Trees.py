from typing import List, Optional

'''
https://leetcode.com/problems/all-possible-full-binary-trees/
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.
Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.
A full binary tree is a binary tree where each node has exactly 0 or 2 children.
  Example 1:
Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Example 2:
Input: n = 3
Output: [[0,0,0]]
  Constraints:
1 <= n <= 20
'''


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	m = {0: [], 1: [TreeNode(0)]}

	def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
		if n % 2 == 0:
			return []
		if n == 1:
			return self.m[1]

		if n not in self.m:
			self.m[n] = []
			for i in range(n):
				l_branch = self.allPossibleFBT(i)
				r_branch = self.allPossibleFBT(n - i - 1)

				for left in l_branch:
					for right in r_branch:
						root = TreeNode(0)
						root.left = left
						root.right = right
						self.m[n].append(root)

		return self.m[n]


if __name__ == "__main__":
	s = Solution()
	print(s.allPossibleFBT(7))
