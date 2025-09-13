names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("write your name")
if user_name in names :
    print(f"Your name is at index {names.index(user_name)}")
else:
    print(f"Your name is not in the list")
