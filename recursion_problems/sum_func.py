# Given an integer, create a function which returns the sum of all the individual digits in that integer. For example: if n = 4321, return 4+3+2+1

def sum_digits(num):
	if num < 10:
		return num
	else:
		return num % 10 + sum_digits(num // 10)

# 5912 will return 17
print(sum_digits(5912))