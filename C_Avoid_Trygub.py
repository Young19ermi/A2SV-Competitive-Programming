

def solve(b):
    return ''.join(sorted(b))


n =int(input())
for _ in range(n):
    a = input().strip()
    b = input().strip()
    print(solve(b))


