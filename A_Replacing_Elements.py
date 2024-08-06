
def c(arr, d):
   
    if max(arr) <= d:
        return "YES"

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] <= d:
                return "YES"

    return "NO"


t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    array = list(map(int, input().split()))
    result = c(array, d)
    print(result)
