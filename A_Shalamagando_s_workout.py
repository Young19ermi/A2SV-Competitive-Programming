n =int(input())
nums = list(map(int, input().split()))
chest = []
biceps = []
back = []



chest.append(nums[0])
for i in range(1,len(nums)):
    if i == 1-1 or i == 4-1 or i == 7-1 or i == 10-1 or i == 13-1 or i == 16-1 or i == 19-1 or i == 22-1 or i == 25-1:
        chest.append(nums[i])
    elif i == 2-1 or i == 5-1 or i == 8-1 or i == 11-1 or i == 14-1 or i == 17-1 or i == 20-1 or i == 23-1:
        biceps.append(nums[i])
    else:
        back.append(nums[i])

c = sum(chest)
bi = sum(biceps)
ba = sum(back)

m = max(c,bi,ba)

if m == c:
    print('chest')
elif m == bi:
    print('biceps')
else:
    print('back')