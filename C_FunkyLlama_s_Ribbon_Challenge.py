
import sys, threading

input = lambda: sys.stdin.readline().strip()
def main():
    length,a,b,c = map(int,input().split())
   
    memo={}

    def dp(length):
        if length in memo:
            return memo[length]

        if length < 0:
            return -float('inf')

        if length == 0:
            return 0
        
        for i in [a,b,c]:
            memo[length] = max(-1, dp(length-i)+1 or -1)
        # print(memo)
        return memo[length]

    print(memo)
    print(dp(length))
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()