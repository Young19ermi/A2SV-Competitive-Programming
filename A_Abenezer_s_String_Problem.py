testcases= int(input())
for _ in range(testcases):
    length = int(input())
    string = input()
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    numbers = []
    for i in range(26):
        numbers.append(i+1)
    dictionary = dict(zip(alphabet,numbers))
    letters = []
    for i in range(len(string)):
        letters.append(dictionary[string[i]])
    letters.sort()
    m = max(letters)
    print(m)

