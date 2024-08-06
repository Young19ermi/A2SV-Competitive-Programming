import string
test = input()

numbers = list(range(1,27))
a= list(string.ascii_lowercase)
m = dict(zip(a,numbers))

nums = []
for n in test:
    nums.append(m[n])
nums.sort(reverse = True)
res = []
maxinum = max(nums)
for n in nums:
    if n == maxinum:
        res.append(n)

result = ""
l = len(res)


for key,items in m.items():
    if items == maxinum:
        result += (key) * l
        break
print(result)