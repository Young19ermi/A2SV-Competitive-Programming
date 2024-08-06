testcase = int(input())
for _ in range(testcase):
    length = int(input())

    test = input()
    vision = []
    p =sum(vision)
   
  
    j = len(test)-1
    for i in range(len(test)):
        if test[i] == 'L':
            vision.append(i)
        else:
            vision.append(j-i) 
    
    left = []
    
    for i in range(len(test)):
        left.append(i) 

    right= left[::-1]
    # print(vision)
    # print(left)
    # print(right)
    # print(p)
    res= []
    for  i in range(len(left)):
        if vision[i] < max(left[i], right[i]):
            p += max(left[i], right[i]) + vision[i]
        res.append(p)
        # print(p)

