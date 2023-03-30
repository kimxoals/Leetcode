# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
	def firstBadVersion(self, n: int) -> int:
		low, high = 0, n
		while low < high:
			m = low + (high - low) // 2
			if isBadVersion(m):
				high = m
				if not (isBadVersion(m - 1)):
					return m
			else:
				low = m + 1
		return n


if __name__ == "__main__":
	s = Solution()
	s.firstBadVersion(5)
