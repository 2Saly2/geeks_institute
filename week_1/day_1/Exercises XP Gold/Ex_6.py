import random ;
win = 0
losses = 0
while True :
        user_number = input("Enter a number from 1-9 (or 'quit' to exit):")
        if user_number.lower() == "quit" :
                  break
        user_number= int(user_number)
        random_number = random.randint(1,9)
        if user_number != "quit":
           user_number = int(user_number)
        if user_number == random_number :
            win += 1
            print("winner")
        else:
            losses += 1
            print(f"loser try again the number was {random_number}")

        print(f"You won {win} times and lost {losses} times.")
        
            
       