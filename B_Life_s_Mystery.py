test = input()
s = []
for n in test:
    if s!= []:
        if n != s[-1]:
            s.append(n)
        else:
            s.pop()
    else:
        s.append(n)
print("".join(s))