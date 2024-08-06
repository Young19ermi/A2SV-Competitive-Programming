def solve(n,m,k):
    res = 0
    mango,avo,ban = 0,0,0
    while n >= 1 and m >= 2 and k >= 4:
        if n >= 1:
            mango += 1
            n -=1
        if m >= 2:
            avo += 1
            m-=2
        if k >= 4:
            ban += 1
            k-=4
    return mango + 2 * avo + 4 * ban
n = int(input())
m = int(input())
k = int(input())
print(solve(n,m,k))