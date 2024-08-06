def solve(x):
    a = []
    while x > 0:
        bit = x % 2
        a.append(bit)
        x //= 2
    

    i = 0
    while i < len(a) - 1:
        if a[i] == 1 and a[i + 1] == 1:
            a[i] = -1
            a[i + 1] = 0
            if i + 2 < len(a):
                a[i + 2] += 1
            else:
                a.append(1)
        i += 1
    

    while a and a[-1] == 0:
        a.pop()
    
    return len(a), a

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        x = int(data[i])
        n, a = solve(x)
        results.append(f"{n}")
        results.append(" ".join(map(str, a)))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()