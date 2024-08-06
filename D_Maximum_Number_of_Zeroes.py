def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def solve(nums1, nums2):
    i,j = 0,0
    d = []
    while i < len(nums1) and j < len(nums2):
        d.append(str(nums[j] + '/' + str(nums1[i])))
        i += 1
        j += 1
    

    

test = int(input())
for _ in range(test):
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    print(solve(nums1,nums2))