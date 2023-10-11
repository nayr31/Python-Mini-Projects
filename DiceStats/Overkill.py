import random

num_dice = 1
sides = 6
mod = 3
overkill_mod = False
    
count, sum, ok = 0, 0, 0
while count < 10**5:
    for _ in range(num_dice):
        while True:
            j = 1+random.randrange(sides)
            if overkill_mod and j == 1:
                ok += 1
            else:
                break
        sum += j
        #print(j)
    sum += mod
    count += 1

print(sum/count)
print(ok/count*100)