import string
testcase= int(input())
for _ in range(testcase):
    n,m = map(int,input().split())
    s = list(input().strip())
    p = list(input().strip())
    init = p[0]
    end = p[-1]
    letters  = list(string.ascii_lowercase)
    num = list(range(0,27))
    n =dict(zip(letters,num))
    

    i = 0
    j = len(s)-1
    if init == 'a':
        init = n['a'] + 1

    elif init == 'z':
        init = n[['n[z]'] - 1]
    else:
        init = n[n[init]-1]
    
    while i < len(s) and j > i:
        if s[i] != init:
            i +=1
            j-=1
        elif s[j] != end:
            j-=1
            i+=1  
   
    if init == 0:
        print('NO')
    else:
        print('YES')

