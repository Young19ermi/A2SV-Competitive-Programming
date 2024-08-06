test = int(input())
for _ in range(test):
    words = input()
    r = list(words.strip())
    
    if len(r) < 10:
        print(words)
    else:
        res = ""
        res += words[0]
        res += str(len(r)-2)
        res += words[-1]
        print(res)