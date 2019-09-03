def fib(x):
    if x < 3:
        return 1
    return fib(x-1) + fib(x-2)
re = fib(8)
print(re)