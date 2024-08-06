def solve(digits):
    res = ""
    n = len(digits)
    for i in range(len(digits)):
        if int(digits[i]) < int(d):

            res += str(digits[:i]) + d + str(digits[i:len(digits)])
            break
        
    else:
        res += str(digits[:]) + d
    return res

testcase = int(input())
for _ in range(testcase):
    n,d = input().split()
    digits = input()
    print(solve(digits))



dfe sovle(n):
res = ""
lenght=len(n)

for n in range(len(digits)):
    if int(digits[i]) < j:
        return "nor"