bdef add(testcases):
    sums = 0 
    l = [n for n in range(1,testcases+1)]
    digits = []
    d = []
    s = []
    for n in l:
        digits.append(str(n))
    
    for n in digits:
        d.append(int(n)%100)
    
    return sum(d)
test = int(input())
for _ in range(test):
    testcases = int(input())
    print(add(testcases))