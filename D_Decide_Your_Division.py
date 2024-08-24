def solve(n):

    c2,c3,c5=0,0,0

    while n%2 == 0:
        n//=2
        c2 += 1

    while n%3 == 0:
        n//=3
        c3 += 1

    while n%5 == 0:
        n//=5
        c5 += 1

    if n!=1:
        return -1
    else:
        return c2+ (2*c3)+ (3*c5)
n = int(input())
for _ in range(n):
    num = int(input())
    print(solve(num))


