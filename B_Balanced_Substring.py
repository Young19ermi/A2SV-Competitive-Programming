n = int(input())
s = input()

max_length = 0
count_zero = 0
count_one = 0
prefix_count = {0: -1}

for i in range(n):
    if s[i] == '0':
        count_zero += 1
    else:
        count_one += 1

    diff = count_zero - count_one
    if diff in prefix_count:
        max_length = max(max_length, i - prefix_count[diff])
    else:
        prefix_count[diff] = i

print(max_length)
