from collections import Counter

def solution(strings):
    count = Counter("".join(strings))
    target = count[strings[0][0]]
    for count in count.values():
        if count % len(strings) != 0:
            return "NO"
    
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    strings = [input().strip() for _ in range(n)]
    print(solution(strings))
