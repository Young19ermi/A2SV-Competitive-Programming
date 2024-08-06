testcase =int(input())
admin = {} 
for _ in range(testcase):
    string = input()
  
    if string not in admin:
        admin[string] = 1
        print("Ok")
    else:
        n = 100
        for i in range(n):
            if string +"1" not in admin:
                print(string + "1")
                break
            while string + "i" in string:
                i += 1
            print(string + "1+i")


testcase = int(input())
for _ in range(testcase):
    n = int(input())
    array= list(map(int, input().split()))
    if n == 1:
            print("YES")
            break
    for i in range(len(array)-1):
        if array[i] != array[i+1]:
            print("YES")
            break
        
        else:
            print("NO")
            break
 