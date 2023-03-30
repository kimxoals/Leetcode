def reverse(x: int) -> int:
	ans = 0
	y = x
	x = abs(x)

	while x > 0:
		last_digit = x % 10
		x = x // 10
		ans = ans * 10 + last_digit
	ans += x

	neg_limit = -0x80000000
	pos_limit = 0x7fffffff

	if y > 0:
		if ans & pos_limit == ans:
			return ans
		else:
			return 0
	else:
		ans *= -1
		if ans & neg_limit == neg_limit:
			return ans
		else:
			return 0



# print(reverse(-38765456))
