# length = int(input())
# test = list(input())
# i = 0
# j = 1
# removed = 0
# initial = len(test)
# while i < len(test) and j < len(test):
#     if test[i] != test[j]:
#         test.remove(test[i])
#         test.remove(test[j])
#         initial -= 2
#         if j == len(test)-2:
#             i-=1
#             j+=1
#         i+=2
#         j+=2
#     else:
#         i+=1
#         j+=1
        
        
# print(initial)


n = int(input())  
s = input().strip()  


num_zeros = s.count('0')
num_ones = s.count('1')


remain = abs(num_zeros - num_ones)


print(remain)


