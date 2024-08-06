# testcase = int(input())
# for _ in range(testcase):
#     length,max_diff = map(int, input().split())
#     a = list(map(int, input().split())) #estimated air temperature
#     b = list(map(int, input().split())) # actual temperature
#     days = {index + 1: value for index, value in enumerate(a)}
#     a.sort()
#     b.sort()
#     zipped = dict(zip(b,a))
#     res = []
#     for i in range(len(b)-1):
#         for key,item in days.items():
#             if item == zipped[b[i]].key():
#                 res.append(key)

#     print(res)
#        # res.append(zipped[b[i].key())
testcase = int(input())
for _ in range(testcase):
    length, max_diff = map(int, input().split())
    a = list(map(int, input().split()))  # estimated air temperature
    b = list(map(int, input().split()))  # actual temperature

    days = {index + 1: value for index, value in enumerate(a)}
    b_sorted = sorted(b)
    a_sorted = sorted(a)

    res = []
    for temp in b_sorted:
        for key, value in days.items():
            if abs(value - temp) <= max_diff:
                res.append(key)
                break

    print(res)
