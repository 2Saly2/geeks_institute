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