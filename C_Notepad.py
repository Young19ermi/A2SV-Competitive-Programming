testcase = int(input())
for _ in range(testcase):
    length =int(input())
    s = input()
    start = 0
    for i in range(2):
        if s[start::] in s[i:]:
            print("Yes")
        start += 1
        
        print("No") 