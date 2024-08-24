def solve(num):
    nums = list(str(num))
  
    for n in nums:
        if n != '4' and n!= '7':
            return 'NO'
    else:
        return "YES"

num =int(input())
print(solve(num))
