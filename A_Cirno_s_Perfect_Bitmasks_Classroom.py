
def solve(num):
    n = list(bin(num)[2:])
    new = [0] * (len(n))
    k = 0
    for i in range(len(n)-1,-1,-1):
        if n[i] == '1':
            new[i] = 1
            break
            
    new =[str(n) for n in new]
    new = "".join(new)

    #print(new)
    if num == 1:
        return 3

    else:
        if bin(num).count('1') > 1:
            return int(new,2)
        else:
            return int(new,2)+1
       
        
    

testcase = int(input())
for _ in range(testcase):
    num = int(input())
    print(solve(num))

# t=int(input())
# for _ in range(t):
#     n=int(input())
    
        
    
#     res=[]
   
#     ans=bin(n)[2:]
  
#     res=['0' for _ in range(len(ans))]
#     for i in range(len(ans)-1,-1,-1):
#         if ans[i]=='1':
#             res[i]='1'
#             break
       
    
#     s=''
#     for i in range(len(res)):
#         s+=res[i]
#     if n==1:
#         print(3)
        
#     else:
#         if n.bit_count()>1:
#             print(int(s,2))
#         elif n.bit_count()==1:
#             print(int(s,2)+1)
  