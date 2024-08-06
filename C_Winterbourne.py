testcase = int(input())
for _ in range(testcase):
    n,m = map(int, input().split()) # n is the number of people, m is the number of chairs.
    mimimum= list(map(int, input().split()))
    if n > m:
        print("NO")
        continue
    total_chair = 0
    
    for i in range(len(mimimum)-1):
        
        total_chair += (2 * mimimum[i]) + 1
    #print(total_chair)
    if total_chair >= m:
        print("NO")
    else:
        print("YES")
