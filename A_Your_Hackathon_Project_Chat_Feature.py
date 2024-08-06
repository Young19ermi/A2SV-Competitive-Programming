def solve(string):
    
    stack =[]
    index = float('inf')
    k = [n for n in string]
    k = k[::-1]
    for i in range(len(k)):
        if k[i] != ')':
            index = i
        
            break
        else:
            stack.append(k[i])
    if len(k)-index < len(stack):
        return 'Yes'
    else:
        return 'No'
    
test = int(input())
for _ in range(test):
    length = int(input())
    string = input()
    print(solve(string))


def solve(string):
    stack = []
    index = float('inf')
    k = [n for n in string]
    k = k[::-1]
    for i in range(len(k)):
        if k[i] != ')':
            index = i
            break
        else:
            stack.append(k[i])

    if len(k) - index < len(stack):
        return 'yes'
    else:
        return 'no'

    nums = [3,4,5,2,6]
    graph = defaultdict(int)
    for n in nums:
        graph[n]