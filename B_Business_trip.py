
k = int(input())
rates = list(map(int, input().split()))

if k == 0:
    print(0)
else:
    rates.sort(reverse=True)

    total= 0
    months = 0

    for rate in rates:
        total += rate
        months += 1
        if total >= k:
            print(months)
            break
    else:
        print(-1)












# k = int(input())
# test = list(map(int, input().split()))
# test.sort(reverse = True)
# maxim = k
# tot = 0
# steps = 0
# maxim = k
# tot = 0
# steps = 0
# for i in range(len(test)):
#     if tot >= maxim:
#         print(steps)
#         break
#     tot += test[i``]
#     steps += 1
# if i == len(test) -1:
#     print(-1)