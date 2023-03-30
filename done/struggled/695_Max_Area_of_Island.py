import collections
from typing import List


class Solution:
	# BFS solution
	def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

		visited = []  # List to keep track of visited nodes.
		queue = collections.deque([(0, 0)])
		visited.append((0, 0))
		res = 0

		while queue:
			i, j = queue.popleft()
			for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
				if grid[x][y] == 1:
					queue.append((x, y))


if __name__ == "__main__":
	s = Solution()
	print(s.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
							 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
							 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
							 [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
							 [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
							 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
							 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
							 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
