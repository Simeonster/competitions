import random
from sys import stdout


def between(l, r):
    print(l, r)
    stdout.flush()

    return input()[0] == 'Y'


def try_small_range(l, r, k):
    idx = random.randrange(l, r+1)

    if between(idx, idx):
        return idx, idx

    return l-k, r+k


def here_for_sure(l, r):
    global k
    global n

    l = max(l, 1)
    r = min(r, n)

    len = r - l + 1
    if len-1 <= 4 * k:
        res = try_small_range(l, r, k)
        return res

    mid = (l + r) // 2
    if between(l, mid):
        return here_for_sure(l-k, mid+k)
    else:
        return here_for_sure(mid+1-k, r+k)


def legit(res):
    return res[0] == res[1]


def main():
    random.seed(22335577)
    global n
    global k

    (n, k) = map(int, input().split())
    cur_range = (1, n)
    res = here_for_sure(cur_range[0], cur_range[1])

    while not legit(res):
        cur_range = res
        res = here_for_sure(cur_range[0], cur_range[1])


try:
    main()
except Exception as e:
    print(e)

