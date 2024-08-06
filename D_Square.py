


    
def solve(x_cor,y_cor):  

    x_cor.sort()
    y_cor.sort()
    p = max(x_cor) - min(x_cor)
    q = max(y_cor) - min(y_cor)
    return p**2
        
testcase = int(input())
x_cor = []
y_cor = []
for _ in range(testcase):
    x,y = map(int, input().split())
    x_cor.append(x)
    y_cor.append(y)
    print(solve(x_cor,y_cor))

