testcases = int(input())
for _ in range(testcases):
    n = int(input())
    p = input()
    points = list(map(int, p.split()))
    points.sort()
    # for the first testcase
    i = 0
    j = 2
    pairs = []
    while j <= len(points)-1:
        pairs.append((points[j],points[i]))
        i += 1
        j += 1
    # while i < len(points):
    #     pairs.append(points[:])
    # while j < len(points)-1:
    #     pairs.append(points[:])
    print(pairs)