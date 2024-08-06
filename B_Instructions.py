

import sys, threading

input = lambda: sys.stdin.readline().strip()
def main():
    
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        memory = [-1]*n

        def dp(idx):
           
            if idx >= n:
                return 0

            if memory[idx] != -1:
                return memory[idx]
            
            memory[idx] = dp(idx + a[idx]) + a[idx]
            return memory[idx]
        
        ans = 0
    
        for start in range(n):
            ans = max(ans, dp(start))
        print(ans)
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()