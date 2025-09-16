import random

def compar_nmb (user_nmb):
    random_nmb = random.randint(1 ,100)
    if user_nmb == random_nmb :
        print("Success! Both numbers are the same.")

    else:
        print(f"Fail! Your number: {user_nmb}, Random number: {random_nmb}")

compar_nmb(20)