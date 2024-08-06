"""
testcase = int(input())
for _ in range(testcase):
    l = int(input())
    
    arr= list(map(int, input().split()))
    arr.sort(key=lambda x:x%2 )
    print(*arr)

  
    """
testcase = int(input())
for _ in range(testcase):
    i = int(input())
odd= []
even =[]
for num in arr:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
even.extend(odd)
print(*even)

if len(odd) > len(even):
    odd.extend(even)
    print(*odd)
else:
    even.extend(odd)
    print(*even)