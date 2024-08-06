cost, initial, wants = map(int, input().split())
total = wants / 2  * (cost + (wants * cost))
if int(total - initial) > 0:
    print(int(total - initial))
else:
    print(0)
