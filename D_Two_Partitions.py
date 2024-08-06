testcase = int(input())

test = list(map(int, input().split()))


positive = [0]
negative= [0]

for n in test:
    if int(n) > 0:
        positive.append(n)
    else:
        negative.append(n)
p = sum(positive)
q = sum(negative)

print(p-q)

        
