from typing import List
from collections import deque


class Solution:
	def rotate1(self, nums: List[int], k: int) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""

		for i in range(k):
			nums.insert(0, nums[-1])
			nums.pop(-1)
		print(nums)

	def rotate2(self, nums: List[int], k: int) -> None:
		items = deque(nums)
		items.rotate(k)
		nums[:] = list(items)
		print(nums)

	def rotate3(self, nums: List[int], k: int) -> None:
		k = k % len(nums)
		l = len(nums)
		for i in range(k):
			nums[i], nums[l - k + i] = nums[l - k + i], nums[i]
			print(nums)
		print(nums)


if __name__ == "__main__":
	s = Solution()
	s.rotate3([1, 2, 3, 4, 5, 6, 7], 1)

'''
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''
