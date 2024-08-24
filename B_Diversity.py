
def solve(s, k):
    unique = set(s)
    current = len(unique)

    if current >= k:
        return 0
    elif k > len(s):
        return "impossible"
    else:
        return k - current

s = input().strip()
k = int(input().strip())

result = solve(s, k)
print(result)