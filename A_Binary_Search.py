length,queries = input().split()
n = list(map(int, input().split()))
nums = list(map(int,input().split()))


for elem in nums:

    i = 0 
    j = len(n)-1

    while i <= j:

        mid = (i+j) // 2

        if n[mid] == elem:
            print('YES')
            break
        elif n[mid] < elem:
            i = mid + 1
            
        else:
            j = mid-1
            
    else:
        print('NO')

