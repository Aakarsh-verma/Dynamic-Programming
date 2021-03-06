# classic
def fibnotsogood(n):
    if n<=2: return 1
    return fib(n-1) + fib(n-2)

# memoization
# python dicts, keys will be arg to fn, val will be the return val
def fib(n, memo={}):
    if n in memo: return memo[n]
    if n<=2: return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))