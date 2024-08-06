test = int(input())
for _ in range(test):
    n,m,k = map(int, input().split())
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))

    count = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] + nums2[j] <= k:
                count += 1
    print(count)