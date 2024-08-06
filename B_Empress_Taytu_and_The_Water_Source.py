# testcase = int(input())
# for _ in range(testcase):
#     n,k = map(int, input().split())
    
#     d = list(map(int, input().split()))
#     a = list(map(int, input().split()))

#     def solve(size):
#         count = 0
#         for i in range(len(d)):
#             while d[i] >0:
#                 d[i] -= size
#                 count += a[i]
#         return count
def is_possible(wagon_size, demand, time, k):
    current_time = 0
    for i in range(len(demand)):
        if demand[i] > 0:
            trips_required = (demand[i] + wagon_size - 1) // wagon_size
            current_time += trips_required * time[i]
            if current_time > k:
                return False
    return True

def min_wagon_size(t, test_cases):
    output = []
    for _ in range(t):
        n, k = test_cases[_][0]
        demand = test_cases[_][1]
        time = test_cases[_][2]
        
        low = 1
        high = max(demand)
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid, demand, time, k):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        output.append(result)
    
    return output