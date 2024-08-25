n = int(input())
res = ""
word = True
if n==1:
    print("I hate it")
for _ in range(n-1):
    if word:
        res += 'I hate'
        word = False
    else:
        res += 'that I love'
        word = True
if (n-1)%2 == 0:
    res += " that I hate it"
    
    print(res)
else:
    res += " that I love it"
    print(res)