# With Recursion
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

print(factorial(4))

# With Reduce
from functools import reduce
def fact(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print(fact(4))

# The math factorial module with python
from math import factorial
print(factorial(4))