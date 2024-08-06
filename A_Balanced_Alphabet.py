import string
t = int(input())
for _ in range(t):
    length, k = map(int, input().split())
    alpha = list(string.ascii_lowercase)
    freq = length // k
    rem = length % k
    ans = ""
    for i in range(k):
        ans += chr(ord('a') + i) * freq
    ans += ans[:rem]
    print(ans)