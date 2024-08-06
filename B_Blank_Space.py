# from collections import Counter
# testcase = int(input())
# for _ in range(testcase):
#     test = input()
#     case = list(map(int,test.split()))
#     #rep = {num:count for num,count in Counter(case)}
#     rep = {num:case.count(num) for num in case}
#     #print(rep)
    
#     for num, value in rep.items():
#         if value == 1:
#             print(num)
#             break
#         else:
#             pass

# question number two

testcase = int(input())
for _ in range(testcase):

    test = input() # row
    col = input()
    for elem in col:
            if elem == "?":
                if "A" and "B" in col:
                    print("C")
                elif "C" and "B" in col:
                    print("A")
                else:
                    print("B")

    # row = len(tested)
    # col =len(tested[0])
    # for col in tested:
    #     for elem in col:
    #         if elem == "?":
    #             if "A" and "B" in col:
    #                 print("C")
    #             elif "C" and "B" in tested[col:]:
    #                 print("A")
    #             else:
    #                 print("B")
            # if tested[row][col] == "?":
            #     if "A" and "B" in tested[col:]:
            #         print("C")
            #     elif "C" and "B" in tested[col:]:
            #         print("A")
            #     else:
            #         # print("B")

#question number three
# from math import sqrt
# testcase = int(input())
# for _ in range(testcase):
#     length= int(input())
#     inputs = input()
#     nums = list(map(int, inputs.split()))
#     res = sqrt(sum(nums))
#     #print(res)
#     if res % 1 == 0:
#         print("YES")
#     else:
#         print("NO")
    # print(modf(res))
    # if isdecimal(res):

    # if isinstance(res, int):
    #     print("YES")
    # else:
    #     print("NO")
        
# question number Four

# def split_into_syllables(word):
#     vowels = {'a', 'e'}
#     result = []
#     i = 0
#     while i < len(word):
#         if word[i] in vowels:  # Vowel
#             if i < len(word) - 1 and word[i + 1] not in vowels:  # CVC
#                 result.append(word[i:i + 3])
#                 i += 3
#             else:  # CV
#                 result.append(word[i:i + 2])
#                 i += 2
#         else:  # Consonant
#             if i < len(word) - 2 and word[i + 1] in vowels and word[i + 2] not in vowels:  # CVC
#                 result.append(word[i:i + 3])
#                 i += 3
#             else:  # CV
#                 result.append(word[i:i + 2])
#                 i += 2
#     return '.'.join(result)

# # Read the number of test cases
# t = int(input())

# Process each test case
# for _ in range(t):
#     n = int(input())
#     word = input().strip()
#     syllables = split_into_syllables(word)
#     print(syllables)




           
    # while i < len(length):
    #     if i + 1 < len(length) and length[i] in C and length[i+1] in V:
    #         if i + 2 < len(length) and length[i+2] in C:
    #             res += length[i] + length[i+1] + length[i+2] + "."
    #             i += 3
    #         else:
    #             res += length[i] + length[i+1] + "."
    #             i += 2
    #     else:
    #         res += length[i] + "."
    #         i += 1
    # print(res)  # Remove the extra dot at the end

   





