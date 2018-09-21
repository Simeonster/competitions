def find_gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r

    return a


(a, b, x, y) = map(int, input().split())
gcd = find_gcd(x, y)

start_w = x / gcd
start_h = y / gcd

max_mult = min(a // start_w, b // start_h)

print (int(max_mult))
