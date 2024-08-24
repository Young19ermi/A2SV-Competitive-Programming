def solve(w):

    A= 0
    D = 0
    for n in w:
        if n == 'A':
            A += 1
        else:
            D += 1
    if A>D:
        return "Anton"
    elif A== D:
        return "Friendship"
    else:
        return "Danik"
n = int(input())
w = input()
print(solve(w))