from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
		left = head
		right = head
		c = 1
		while right.next is not None:
			right = right.next
			c += 1

			if c % 2 == 0:
				left = left.next
		return left


if __name__ == "__main__":
	s = Solution()
