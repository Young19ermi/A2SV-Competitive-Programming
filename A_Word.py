
def solve(test):
    lower = 0
    upper =  0
    for n in test:
        if  n.islower():
            
            lower += 1
        else:
            upper += 1 
    res = ""
 
    if lower >= upper:
        return test.lower()
    else:
        return test.upper()

test= input()


print(solve(test))