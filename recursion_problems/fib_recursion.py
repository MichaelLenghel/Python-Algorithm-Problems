def fib(num):
	if num == 1:
		return 1
	return num + fib(num - 1)

print(fib(5))