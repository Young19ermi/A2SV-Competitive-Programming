def solve(word):
    word = list(word)
    if len(set(word)) == 1:
        return -1
    if word != word[::-1]:
        return "".join(word)
    
    if word == word[::-1]:
        l = list(sorted(word))
        return ''.join(l)
n = int(input())
for _ in range(n):
    word = input()
    print(solve(word))


