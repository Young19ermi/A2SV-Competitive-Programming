testcases = int(input())
for _ in range(testcases):
    s =input()
    d = "codeforces"
    count = 0
    for i in range(len(s)): 
        if d[i] != s[i]:
            count += 1 
    print(count)
    

