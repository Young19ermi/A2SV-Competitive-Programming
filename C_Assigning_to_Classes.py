t = int(input())  

for _ in range(t):
    n = int(input())  
    skills = list(map(int, input().split()))  

    skills.sort()  

    index = n - 1
    m = skills[index]

    f = float('inf')

    for i in range(n):
        diff = abs(skills[i + n] - m)
        f = min(f, diff)

    print(f)
