
def solve(str,s):
    l = list(str)
    m = list(s)
    check = True
    for i in range(len(l)):
        if l[i] != m[i]:
            check = False
    
    if check:
        return 0
    # to check the lexiographic sesquence we can just check string 1 < string 2
    if str < s:
        return -1
    else:
        return 1

str = input().lower()
s = input().lower()

print(solve(str,s))