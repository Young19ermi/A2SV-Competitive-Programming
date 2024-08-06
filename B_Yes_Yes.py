t = int(input())
for _ in range(t):
    n = input()
    string = "Yes" * len(n)
    if n in string:
        print("YES")
    else:
        print("NO")