def dp(i,j,n,m,count):
    count = 0
    if i == n-1 or j == m-1:
        return 1
    
    if i == n or j == m:
        return -1
    else:
        left_move = dp(i+1,j,n,m,count + j)
        right_move = dp(i,j+1,n,m,count + i)
        
        return count

n = int(input())
for _ in range(n):
    n,m,k = map(int, input().split())
    count = 0
    if n*m -1 == k:
        print('YES')
    else:
        print('NO')


import sys, threading
input = lambda: sys.stdin.readline().strip()


def main():
    
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        memo = [-1]*n

        def dp(idx):
            # base case
            if idx >= n:
                return 0

            if memo[idx] != -1:
                return memo[idx]
            
            memo[idx] = dp(idx + a[idx]) + a[idx]
            return memo[idx]
        
        ans = 0
        for start in range(n):
            ans = max(ans, dp(start))
        
        print(ans)

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join