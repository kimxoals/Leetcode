from typing import List
from collections import deque


class Solution:

	# BFS solution
	def floodFill_BFS(self, image: List[List[int]], sr: int, sc: int,
					  color: int) -> List[List[int]]:
		old_color = image[sr][sc]
		if old_color != color:
			queue = deque([(sr, sc)])
			while queue:
				i, j = queue.popleft()
				image[i][j] = color
				for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
					if 0 <= x < len(image) and 0 <= y < len(image[x]):
						if image[x][y] == old_color:
							queue.append((x, y))
		return image

	# DFS solution
	def floodfill_DFS(self, image: List[List[int]], sr: int, sc: int,
					  color: int) -> List[List[int]]:
		def dfs(i, j):
			image[i][j] = color
			for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
				if 0 <= x < len(image) and 0 <= y < len(image[x]):
					if image[x][y] == old_color:
						dfs(x, y)

		old_color = image[sr][sc]
		if old_color != color:
			dfs(sr, sc)
		return image


if __name__ == "__main__":
	s = Solution()

	print(s.floodfill_DFS([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
