def max_fireworks(a, b, m):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    lcm = (a * b) // gcd(a, b)
    first = m // a
    second = m // b
    common = m // lcm

    result = first + second - 2 * common + 1

    return result

t = int(input())

for _ in range(t):
    a, b, m = map(int, input().split())
    print(max_fireworks(a, b, m))
