from typing import List


class Solution:
	def search(self, nums: List[int], target: int) -> int:
		low = 0
		high = len(nums)
		while True:
			m = (low + high) // 2
			print(m, low, high)
			if target < nums[m]:
				high = m
			elif target > nums[m]:
				low = m + 1
			else:
				return m
			if low == high:
				break
		return -1


if __name__ == "__main__":
	s = Solution()
	s.search([-1, 0, 3, 5, 9, 12], 2)
