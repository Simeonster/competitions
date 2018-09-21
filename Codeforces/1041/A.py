from functools import reduce

n = int(input())
numbers = list(map(int, input().split()))

mn = reduce(lambda accum, value: min(accum, value), numbers)
mx = reduce(lambda accum, value: max(accum, value), numbers)

print(mx - mn + 1 - n)
