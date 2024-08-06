testcase = int(input())
for _ in range(testcase):
    string = str(input())
    string.lower()
    check = ["c","o","d","e","f","o","r","c","e","s"]
    if string in check:
        print("YES")
    else:
        print("NO")