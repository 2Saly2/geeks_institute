birthdays ={
    "nouhaila": "23/12/2001" ,
    "sarah":"5/5/2001",
    "karim":"22/8/2008",
    "ali":"3/6/1999",
    "mariya": "13/1/2003"
}
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
