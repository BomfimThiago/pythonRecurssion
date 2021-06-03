def countdown(n):
    print(n)
    if n > 0:
        countdown(n - 1)

countdown(5)

# The base case is when n is 0
# The argument always changes so that each
# recursion moves closer to the base case

