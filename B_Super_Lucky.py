n = input()
def checker(target):
    count = 0
    for l in str(target):
        count += 1
    k = list(o for o in str(target))
    four,seven =0,0
    for i in k:
        if i == '4':
            four += 1
        elif i == '7':
            seven += 1

    flag = False
    if count % 2 == 0 and four == seven:
        flag =True
    return flag

if checker(n):
    print(n)
else:
    count = 0
    for l in str(n):
        count += 1
    i = int(n)
    j = 10**count

    while j > i+1:

        mid = (i+j) // 2

        if checker(mid):
            j = mid
        else:
            i = mid
    
    while j > i+1:

        mid = (i+j) // 2

        if checker(mid):
            j = mid
        else:
            i = mid
    print(j)