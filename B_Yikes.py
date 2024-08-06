n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))


prefix_sum = [0]
for pile in a:
    prefix_sum.append(prefix_sum[-1] + pile)


for label in q:
    low = 0
    high = n

    while low <= high:
        mid = low + (high - low)//2
        if prefix_sum[mid] < label:
            low = mid + 1
        
        else:
            high = mid - 1
    
    print(low)


    test = int(input())

    for _ in range(testcase):
        string  = input()

        for n in range(len(string)):
            