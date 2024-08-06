from collections import Counter

    
n,m = input().split()
s = input()

count = [s.count(chr(i)) for i in range(ord('A'), ord('A')+ int(m))]

print(min(count)*int(m))