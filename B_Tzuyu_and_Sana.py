k = int(input())
for _ in range(k):
    n,m = input().split()
    print((int(n)^(int(n)&int(m))) + (int(m)^(int(n)&int(m))))