# Exercise 1 :
s="Volkswagen,Toyota,Ford Motor,Honda,Chevrolet"
c=["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
cars=s.split(",")
print(cars)
print(f"we have {len(cars)}companies")
print(sorted(cars, key=None, reverse=True))


count_o=0
count_i=0
list_o=[]
list_i=[]
for car in cars:
    if "o" in car.lower():
        count_o+=1
        list_o.append(car)    
       
    elif "i"  not in car.lower():
         count_i+=1
         list_o.append(car)
        
print(f"companies have letter O {list_o}")   
print(f"companies have not letter i {list_i}")
print(f"{count_o} companies have letter O")
print(f"{count_i} companies have letter i")


set_cars =list(set(c))
result = ", ".join(set_cars)
print(set_cars)
print(result)

# Exercise 2 :

def get_full_name(first_name, last_name,middle_name=None):

    first_name=first_name.strip().capitalize()
    last_name=last_name.strip().capitalize()

    if middle_name :
        middle_name=middle_name.strip().capitalize()
        full_name= f"{first_name} {middle_name} {last_name}"
    else:
        full_name=f"{first_name} {last_name}"
    return full_name

print(get_full_name("mohamed","ali","ahmed"))
print(get_full_name("mohamed","ali"))
