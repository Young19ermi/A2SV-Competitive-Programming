from heapq import heapify,heappop,heappush

test = int(input())
for _ in range(test):
    command,val = input().split()
    print(command)
    q = []
    heapify(q)
    
    if command == 'insert':
        heappush(q,val)
    elif command  == 'removeMin':
        heappop(q)
    else:
        k = q[0]
print(q)