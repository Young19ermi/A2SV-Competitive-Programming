def solve(words):
    n = []
    m = []
    x=len(words)//2
    
    if len(words) % 2 == 0:
        for i in range(len(words)//2):
            n.append(words[i])
        for j in range(x,len(words)):
            m.append(words[j])
        i = 0
        j = 0
        while i < len(n) and j < len(m):
            if n[i] != m[j]:
                return 'NO'
                break
            i+=1
            j+=1
        return 'YES'
    else:
        return 'NO'

t = int(input())
for _ in range(t):
    words = input()
    print(solve(words))