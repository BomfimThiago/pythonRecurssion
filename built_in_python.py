# A way to know the recursion limit
from sys import getrecursionlimit
print(getrecursionlimit())

# A way to change the recursion limit
from sys import setrecursionlimit
setrecursionlimit(2000)
print(getrecursionlimit())