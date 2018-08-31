# Calculates fibonacci sequence using memoization for time efficiency
# This works in python as it's functions are treated as first class objects, much like Perl

def fib(num):
	memo = {}
	if num == 1:
		return 1

	if not num in memo:
		memo[num] = num * fib(num - 1)
	return memo[num]

print(fib(5))