import string
testcase = int(input())
for _ in range(testcase):
    n = int(input())
    alphabet = list(string.ascii_lowercase)
    nums = list(range(1, 27))
    m = dict(zip(nums,alphabet))
    check = 0
    res = ""
    if n < 26:
        check += 26 - n
        res += (m[check]) * 2 + m[n]
    else:
        
    print(res)
    
   
    
        

