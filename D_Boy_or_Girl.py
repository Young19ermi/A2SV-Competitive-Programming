test = input()


g = list(set(test))

if len(g) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print('IGNORE HIM!')