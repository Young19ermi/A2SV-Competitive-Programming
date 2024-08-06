def binary_search(arr, target):
    i = -1
    j = len(arr)

    while j > i+1:

        mid = (i+j) //2

        if arr[mid] < target:
            i = mid
        else:
            j= mid

    return j+1

n, k = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))


for query in queries:
    index = binary_search(arr, query)
    print(index)