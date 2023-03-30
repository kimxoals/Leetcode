from typing import List


class Solution:
	def sortedSquares(self, nums: List[int]) -> List[int]:
		res = [0] * len(nums)
		left, right = 0, len(nums) - 1
		while left <= right:
			res[right - left] = max(abs(nums[left]), abs(nums[right])) ** 2
			if abs(nums[left]) > abs(nums[right]):
				left += 1
			else:
				right -= 1
		return res


if __name__ == "__main__":
	s = Solution()
	print(s.sortedSquares([-4, -1, 0, 3, 10]))
