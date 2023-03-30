from typing import List


class Solution:
	# TLE bad solution
	def lengthOfLongestSubstring1(self, s: str) -> int:
		size = len(s)
		while size > 1:
			for i in range(len(s) - size + 1):
				if len(set(s[i:i + size])) == len(s[i:i + size]):
					return size
			size -= 1
		return size

	def lengthOfLongestSubstring2(self, s: str) -> int:
		used = {}
		start = max_length = 0

		for i, c in enumerate(s):
			if c in used and start <= used[c]:
				start = used[c] + 1
			else:
				max_length = max(max_length, i - start + 1)
			used[c] = i

		return max_length


if __name__ == "__main__":
	s = Solution()
	print(s.lengthOfLongestSubstring2("aaabb"))
