# Exercise 1 :

birthdays ={
    "nouhaila": "23/12/2001" ,
    "sarah":"5/5/2001",
    "karim":"22/8/2008",
    "ali":"3/6/1999",
    "mariya": "13/1/2003"
}
print("Welcome ! you can look up birthdays ")
user_name = input("enter your name :").strip().lower()
if user_name in birthdays.keys():
    bday= birthdays.get(user_name,"")
    print(f"{user_name} 's birthday is {bday}")
else:
    print(f"Sorry, we don't have the birthday information for {user_name}")

# Exercise 2 :

print("\nnames :\n","\n".join(birthdays.keys()))

name=input("enter your name !").strip().lower()
if name in birthdays.keys():
    bday= birthdays.get(name,"")
    print(f"{name} 's birthday is {bday}")
else:
    print(f"Sorry, we don't have the birthday information for {name}")
    new_bday = input("Please enter their birthday (dd/mm/yyyy): ").strip()
    birthdays[name] = new_bday
    print("\nBirthday added successfully! ")
    print("\nnames :\n","\n".join(birthdays.keys()))

    # Exercise 3:

def play_nmb(X):
    s=str(X)
    total =int(s)+int(s*2)+int(s*3)+ int(s*4)
    print(s)
    return total
   
print(play_nmb(3))

# Exercise 4 :

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

