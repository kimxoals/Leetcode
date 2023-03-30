from typing import List
from collections import Counter


class Solution:
	def checkInclusion(self, s1: str, s2: str) -> bool:
		counter, end, count = Counter(s1), 0, 0
		while end < len(s2):
			if s2[end] in counter:
				counter[s2[end]] -= 1
				if counter[s2[end]] == 0:
					count += 1
			if end >= len(s1) and s2[end - len(s1)] in counter:
				if counter[s2[end - len(s1)]] == 0:
					count -= 1
				counter[s2[end - len(s1)]] += 1
			if count == len(counter):
				return True

			end += 1
		return False


if __name__ == "__main__":
	s = Solution()
	print(s.checkInclusion("ab", "adbdaaabbb"))
