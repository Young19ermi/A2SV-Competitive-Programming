n = int(input())
for _ in range(n):
    length = int(input())
    nums= list(map(int, input().split()))
    num = list(map(int, input().split()))

    count = 0
    for i in range(len(nums)-1):
        temp = num[i]
        if temp > num[i]:
            for j in range(i,len(num)-1):
                if temp > num[j]:
                    count += 1
                else:
                    temp = nums[i+1]
                    break
    print(count)