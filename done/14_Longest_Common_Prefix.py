from typing import List


class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		i = 0
		while True:
			try:
				r = strs[0][i]
				for s in strs:
					if s[i] != r:
						return strs[0][:i]
				i += 1
			except IndexError:
				return strs[0][:i]

	def longestCommonPrefix2(self, strs: List[str]) -> str:
		# reduce prefix from full length
		prefix = strs[0]
		for _ in range(len(prefix)):
			for s in strs[1:]:
				if prefix != s[:len(prefix)]:
					prefix = prefix[:-1]
		return prefix


if __name__ == "__main__":
	s = Solution()
	print(s.longestCommonPrefix2(["flower", "flew", "float"]))
