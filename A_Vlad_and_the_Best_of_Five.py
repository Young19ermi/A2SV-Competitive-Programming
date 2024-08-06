testcases = int(input())
for _ in range(testcases):
    test = input()
    if test.count('A') > test.count('B'):
        print('A')
    else:
        print('B')

