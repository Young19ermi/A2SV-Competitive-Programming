test  = input()
res = ""

if test[0].isupper():
    
    print(test)
else:
    new = test[0].upper()
  
    res += new
    res += test[1:]
    print(res)