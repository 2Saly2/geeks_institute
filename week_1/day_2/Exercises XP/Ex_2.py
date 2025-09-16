family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 3}
total=0
for name, age in family.items():
   if age < 3:
        price = 0
        print(f"The ticket is free for {name}")
   elif 3 <= age <= 12:
        price = 10
        print(f"{name}'s ticket price is $10")
   else:
        price = 15
        print(f"{name}'s ticket price is $15")
   total+= price
print(f"total of tickets for your family is {total}")

########## Bonus:

total=0
family={}
nmp_of_people=int(input("How many family members do you want to add?"))

for i in range(nmp_of_people):
    name=input("enter your name")
    age = int(input("enter your age"))
    family[name]=age
 
for name, age in family.items():
    if age < 3:
        price = 0
        print(f"The ticket is free for {name}")
    elif 3 <= age <= 12:
        price = 10
        print(f"{name}'s ticket price is $10")
    else:
        price = 15
        print(f"{name}'s ticket price is $15")
        
    total+=price
print(f"total of tickets for your family is {total}")