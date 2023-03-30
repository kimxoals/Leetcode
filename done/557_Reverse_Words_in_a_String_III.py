from typing import List


class Solution:
	def reverseWords(self, s: str) -> str:
		line = s.split()
		for i, word in enumerate(line):
			left, right = 0, len(word) - 1
			word = list(word)
			while left < right:
				word[left], word[right] = word[right], word[left]
				left += 1
				right -= 1
			line[i] = ''.join(word)
		return ' '.join(line)

	def reverseWords2(self, s: str) -> str:
		return ' '.join(s.split()[::-1])[::-1]


if __name__ == "__main__":
	s = Solution()
	print(s.reverseWords2("Let's take LeetCode contest"))
