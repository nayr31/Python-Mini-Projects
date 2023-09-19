import random

while True:
    try: 
        sides = int(input("How many sides on the dice? "))
        break
    except:
        print("Not a valid input, must be a number.")
    
count, sum = 0, 0
while count < 10**6:
    sum += max(random.randrange(sides+1), random.randrange(sides+1))
    count += 1

print("Average of rolling two dice and taking the result is:")
print(sum / 10**6)