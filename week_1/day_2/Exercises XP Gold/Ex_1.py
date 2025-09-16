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