from typing import List


class Solution:
	# Brute force
	def twoSum1(self, numbers: List[int], target: int) -> List[int]:
		for i, x in enumerate(numbers):
			for j, y in enumerate(numbers):
				if (x + y == target) and (i != j):
					return [i, j]

	# Binary search
	def twoSum2(self, numbers: List[int], target: int) -> List[int]:
		for i, x in enumerate(numbers):
			diff = target - x
			left, right = i + 1, len(numbers) - 1
			while left < right:
				mid = left + (right - left) // 2
				if numbers[mid] >= diff:
					right = mid
				else:
					left = mid + 1
			if numbers[left] == diff:
				return [i + 1, left + 1]

	def twoSum3(self, numbers: List[int], target: int) -> List[int]:
		left, right = 0, len(numbers) - 1

		while left < right:
			sum = numbers[left] + numbers[right]
			if sum > target:
				right -= 1
			elif sum < target:
				left += 1
			else:
				return [left + 1, right + 1]


if __name__ == "__main__":
	s = Solution()
	print(s.twoSum3([2, 7, 11, 15], 9))
