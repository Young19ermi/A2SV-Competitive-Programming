# testcase = int(input())
# for _ in range(testcase):
#     n = input()
#     x, y =map(int, input().split())
#     points = [x,y]
#     count = []
#     for x in points:
#         for y in points:
#             if x<0 and y<0:
#                 count.append("A")
#             elif x>0 and y<0:
#                 count.append("B")
#             elif x<0 and y>0:
#                 count.append("C")
#             elif x==0 and y==0:
#                 count.append("zeros")
#             else:
#                 count.append("D")
#     print(points)

def can_reach_all_points(n, points):
    x_coords = set()
    y_coords = set()
    for point in points:
        x, y = point
        x_coords.add(x)
        y_coords.add(y)
    if len(x_coords) > 1 and len(y_coords) > 1:
        return "NO"
    
    else:
        return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    result = can_reach_all_points(n, points)
    print(result)
