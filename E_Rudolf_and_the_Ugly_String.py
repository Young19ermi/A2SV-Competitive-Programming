t = int(input())
for _ in range(t):
    length = int(input())
    test = input()
    k = test.count('mapie')
    count = 0
    for i in range(len(test)-2):
        if test[i] == 'm' and test[i+1] == 'a' and test[i+2] == 'p':
            count += 1
        elif test[i] == 'p' and test[i+1] == "i" and test[i+2] == "e":
            count += 1

    print(count - k)