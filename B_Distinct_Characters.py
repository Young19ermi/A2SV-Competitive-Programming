from collections import Counter
s = list((input()))
# print(s)
# ans = []
l = 0
r = 1
counter = Counter(s)
while r < len(s):
    if s[l] != s[r]:
        counter[s[l]] -=1 

        
    else:
        while r < len(s) and  s[l] == s[r]:
            r +=1
        diff = r - l
        if diff % 2 == 0:
            diff //= 2
            for i in range(l, r,2):
                s[i] = chr(ord(s[i]) + 1)
        else:
            if (diff//2) % 2 == 1:
                count = 0
                diff //=2
                step = 1
                s[l+diff] = chr(ord(s[diff]) + 1)
                count +=1
                step = 1
                while count < diff:
                    s[diff + (2 * step)] = chr(ord(s[diff + (2 * step)]) +  1)
                    s[diff - (2 * step)] = chr(ord(s[diff - (2 * step)]) +  1)
                    count += 2
                    step += 1
            else:
                count = 0
                diff //=2
                step = 1
                
                # step = 1
                while count < diff:
                    s[l + (diff + (1 * step))] = chr(ord(s[l + (diff + (1 * step))]) +  1)
                    s[1 + (diff - (1 * step))] = chr(ord(s[l + (diff - (1 * step))]) +  1)
                    count += 2
                    step += 1
    l = r 
    r += 1
print(''.join(s))


                        
                    


                

