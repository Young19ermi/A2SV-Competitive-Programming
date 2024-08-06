
def solve(a,b):
    if a == b:
        return a

    if b % a != 0:
        return 1
    else:
        while b % a != 0:
            b = b // a
        if b == 1:
            return a
        else:
            return 1 



a,b = map(int, input().split())
print(solve(a,b))



# def gcdExtended(a, b): 
   
#     if a == 0 : 
#         return b,0,1
             
#     gcd,x1,y1 = gcdExtended(b%a, a) 
     
  
#     x = y1 - (b//a) * x1 
#     y = x1 
     
#     return gcd,x,y 