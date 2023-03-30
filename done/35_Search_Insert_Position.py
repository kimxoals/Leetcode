from typing import List


class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		def condition(value) -> bool:
			pass

		left, right = 0, len(nums)
		while left < right:
			mid = left + (right - left) // 2
			if nums[mid] >= target:
				right = mid
			else:
				left = mid + 1
		return left


if __name__ == "__main__":
	s = Solution()
	print(s.searchInsert([1, 3, 5, 6], 7))
