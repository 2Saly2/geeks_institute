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