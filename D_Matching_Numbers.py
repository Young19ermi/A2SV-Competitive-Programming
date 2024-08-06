t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        print("No")
        continue
    print("Yes")
    sums = []
    n = len()
    num = set(sums(range(1,2*n))) // n
    add = 0 - add
    

    # print("Yes")
    # left_shift = (n + 1) // 2 # n=1 --->
    # right_shift = -n + left_shift #1

    # left = 1
    # right = n + left_shift
    # switched = True
    # cnt = 0
    # while cnt < n:
    #     print(left, right)
    #     cnt += 1
    #     if switched:
    #         left += left_shift
    #         right += right_shift
    #     else:
    #         left += right_shift
    #         right += left_shift
    #     switched ^= True



# # input
#                 4
# 1
# 2
# 3
# 4
# # expected output
# Yes
# 1 2
# No
# Yes
# 1 6
# 3 5
# 4 2
# No
# # recieved output
# No
# Yes
# 1 2
# 1 2
# No
# Yes
# 1 2
# 1 2
# 3 4
# 3 4

