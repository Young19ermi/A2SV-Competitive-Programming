"""
testcase = int(input())
for _ in range(testcase):
    string = input()
    res= ""
    ans = ""
    count = 0
    n = len(string)-1
    if len(string) < 10:
        res += str(string)
        print(res)
    elif len(string) > 10:
        count = str(len(string) - 2)
        ans += (string[0] + count + string[n])
        print(ans)
"""
