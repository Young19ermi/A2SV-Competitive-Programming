# inputs =input()
# strength,length = map(int, inputs.split())
# for _ in range(length):
#     testme = input()
#     dragonstrength,bonus = map(int, testme.split())
#     if strength < dragonstrength:
#         print("NO")
#         break
#     else:
#         strength += bonus
# else:
#     print("YES")
inputs =input()
strength,length = map(int, inputs.split())
d = []
for _ in range(length):
    testme = input()
    dragonstrength,bonus = map(int, testme.split())
    
    d.append((dragonstrength,bonus)) # inserted as a tuple
d.sort()
for n in d:
    if strength < n[0]:
        print("NO")
        break
    else:
        strength += n[1]
        
else:
    print("YES")
        
# import heapq

# inputs = input()
# player_strength, num_dragons = map(int, inputs.split())

# dragons = []
# for _ in range(num_dragons):
#     dragon_info = input().split()
#     dragon_strength, dragon_bonus = map(int, dragon_info)
#     dragons.append((dragon_strength, dragon_bonus))

# dragons.sort()  # Sort dragons by their strength

# for dragon in dragons:
#     if player_strength > dragon[0]:
#         player_strength += dragon[1]
#     else:
#         print("NO")
#         break
# else:
#     print("YES")

        

