def find_sequence_exists(n, k, b):
    product = 2023
    for i in range(n):
        product //= b[i]

    if product != 1 or k > n:
        return "NO"
    else:
        return "YES\n" + " ".join(str(2023 // x) for x in b[:k])

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    print(find_sequence_exists(n, k, b))

