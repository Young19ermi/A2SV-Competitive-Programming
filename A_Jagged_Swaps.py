testcases = int(input())
for _ in range(testcases):
    length = input()
    for _ in range(int(length)):
        a = list(map(int, input().split()))
        for i in range(2,len(a)-1):
            #a = list(map(int, input().split()))
            # if a.sort() == a:
            #     print("YES")
            #     break
            # elif max(a) != len(a):
            #     print("NO")
            #     break
            if a[i-1] < a[i] and a[i] > a[i+1]:
                a[i] = a[i+1]
                a[i+1] = a[i]
    
        if a == sorted(a):
            print("YES")
            break
        else:
            print("NO")
            break
            
