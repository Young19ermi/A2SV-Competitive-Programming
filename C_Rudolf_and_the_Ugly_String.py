def solve(s):
    tot = len(s)
    c = ''.join(s.split('map'))
    p = ''.join(s.split('pie'))
    if 'pie' not in s and 'map' not in s:
        return 0
    count = 0
    count += c.count('')
    count += p.count('')
    res = 0
 
    if p  == 'ma' and c == 'ie':
        res += ((tot - len(c))//3 + (tot - len(p))//3) // 2

    else:   
        res += (tot - len(c))//3 + (tot - len(p))//3
    return res

testcase = int(input())
for _ in range(testcase):
    length = int(input())
    s = input()
    print(solve(s))