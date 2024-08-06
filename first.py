from collections import Counter
def solve(word):
    res = ""
    res += word[0]
    k = Counter(word)
    k[word[0]] -= 1
    
    
    for key,items in sorted(k.items()):
        if items != 0:
            res +=  key
    return res 

testcase = int(input())
word = input()
print(solve(word))