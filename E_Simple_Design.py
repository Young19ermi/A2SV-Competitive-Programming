def digit(n):
    return sum(int(d) for d in str(n))

def find_k(x, k):
    while True:
        if digit(x) % k == 0:
            return x
        x += 1


t = int(input())
for _ in range(t):
    x, k = map(int, input().split())
    result = find_k(x, k)
    print(result)
