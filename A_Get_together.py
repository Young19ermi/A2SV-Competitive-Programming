def find_min_time(x, v):
    n = len(x)
    
    def can_meet(time):
        left, right = -1e9, 1e9
        for i in range(n):
            l, r = x[i] - time * v[i], x[i] + time * v[i]
            if l > right or r < left:
                return False
            left = max(left, l)
            right = min(right, r)
        return True
    
    lo, hi = -0.1, 1e9
    iterations = 100
    
    for _ in range(iterations):
        mid = lo + (hi - lo) / 2
        if can_meet(mid):
            hi = mid
        else:
            lo = mid
            
    return hi

while True:
    try:
        n = int(input())
        x, v = [], []
        for _ in range(n):
            xi, vi = map(int, input().split())
            x.append(xi)
            v.append(vi)
        
        result = find_min_time(x, v)
        print(f"{result:.20f}")
    except EOFError:
        break
def find_min_time(x, v):
    n = len(x)
    
    def can_meet(time):
        left, right = -1e9, 1e9
        for i in range(n):
            l, r = x[i] - time * v[i], x[i] + time * v[i]
            if l > right or r < left:
                return False
            left = max(left, l)
            right = min(right, r)
        return True
    
    lo, hi = -0.1, 1e9
    iterations = 100
    
    for _ in range(iterations):
        mid = lo + (hi - lo) / 2
        if can_meet(mid):
            hi = mid
        else:
            lo = mid
            
    return hi

while True:
    try:
        n = int(input())
        x, v = [], []
        for _ in range(n):
            xi, vi = map(int, input().split())
            x.append(xi)
            v.append(vi)
        
        result = find_min_time(x, v)
        print(f"{result:.20f}")
    except EOFError:
        break
