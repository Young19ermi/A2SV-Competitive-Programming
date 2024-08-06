# test =  int(input())
# for _ in range(test):
#     length =int(input())
#     for _ in range(length):
#         num = list(input().split())
#         case = True
#         hash = set()
#         for n in num:
#             if n in hash:
#                 case = False
#             else:
#                 hash.add(n)
#         if case:
#             print("YES")
#             break
#         else:
#             print("NO")
#             break
test = int(input())
for _ in range(test):
    length = int(input())
    for _ in range(length):
        num= list(input().split())
        case = True
        hash = set()
        for n in num:
            if n in hash:
                print("NO")
                break
            else:
                hash.add(n)
                break
        print("Yes")
        
        