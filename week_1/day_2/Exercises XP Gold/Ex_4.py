import random

def throw_dice():
    return random.randint(1,6)

def throw_until_doubles():
    count = 0
    while True :
        count+=1
        die1 = throw_dice()
        die2 = throw_dice()
        if die1==die2:
         return count

results =[]
for _ in range(100):
    results.append(throw_until_doubles())

total_throws = sum(results)
average_throws = total_throws/100

print("total throws :", total_throws)
print("average throws :" , round(average_throws , 2))