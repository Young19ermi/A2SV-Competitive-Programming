r = int(input())
arr= list(map(int, input().split()))
maximum = max(arr)
res= 0
for i in range(len(arr)):
    diff = maximum - arr[i]
    res+=diff
print(res)

