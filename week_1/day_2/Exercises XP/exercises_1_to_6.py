# Exercise 1 : Create a dictionary from two lists

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
zipped_dict = zip(keys , values)
print(dict(zipped_dict))

# Exercise 2:

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

# Exercise 3 :

brand ={
   "name": "Zara ",
    "creation_date": 1975 ,
    "creator_name": "Amancio Ortega Gaona" ,
    "type_of_clothes": ["men", "women", "children", "home" ],
    "international_competitors":[ "Gap", "H&M"," Benetton" ],
    "number_stores": 7000 ,
    "major_color": 
        {"France":" blue",
         "Spain": "red", 
         "US":[ "pink", "green"]}

}
brand["number_stores"]=2
print(brand)
#solution 1
type_clothes=brand["type_of_clothes"]
print("zara's client are :")
for c in type_clothes:
    print('-', c)
  #solution 2   
print(f"Zara's clients are {",".join(brand.get('type_of_clothes', []))}")

# brand["country_creation"]= "Spain"
brand.setdefault("country_creation", "Spain")
print(brand)

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
print(brand["international_competitors"])

#Delete the information about the date of creation.
del brand["creation_date"]

print("the last competitor is : ", brand["international_competitors"][-1])

print("the major clothes colors in the US are : " , brand["major_color"]["US"])
print("Number of key-value pairs:", len(brand))
print("keys of brand are : ",list(brand.keys()))

more_on_zara ={
    "creation_date":1975 ,
    "number_stores" : 10000,
}
brand.update(more_on_zara)

print("number of stores:", brand["number_stores"])



# Exercise 4 :

def describe_city(city , country):
    print(f"{city} is in {country}")

describe_city("Rabt","Morocco")


# Exercise 5:

import random

def compar_nmb (user_nmb):
    random_nmb = random.randint(1 ,100)
    if user_nmb == random_nmb :
        print("Success! Both numbers are the same.")

    else:
        print(f"Fail! Your number: {user_nmb}, Random number: {random_nmb}")

compar_nmb(20)


# Exercise 6:

def make_shirt(size="Large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}")

make_shirt()
make_shirt("Medum")
make_shirt("smull", "How are you?") 
make_shirt(text="python" , size="XXL")


