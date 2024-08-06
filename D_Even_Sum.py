"""
x = int(input())
x.sort(key =lambda x:x%2)
total = 0
for i in range(len(x)):
    total += x[i]
    if total % 2 == 0:
        print(total)
    else:
        total - x[0]
        print(total)


testcase = int(input())
for _ in range(testcase):
     #x=int(input())
     x = list(map(int, input().split()))
     x.sort(key =lambda x:x%2)
     total = 0
for i in range(len(x)):
    total += x[i]
    if total % 2 == 0:
        print(total)
    else:
        total = total - x[0]
        print(total)



list(sorted(lambda x:x%2 == 0,input().split()))

#lambda sorting
"""
testcase = input()
num = list(map(int(input())))

x = sorted(list(filter(lambda x:x%2 == 0, num))) # this values are even
nums= sorted(list(filter(lambda x:x%2 != 0, num))) # otherwise they are odd
nums.extend(x)
total = 0
for i in range(len(nums)):
	total += nums[i]
if total % 2== 0:
	print(total)
else:
	total = total - nums[0]
	print(total)
	
