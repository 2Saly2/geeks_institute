import random
class Game:
    pass
    def get_user_item(self):
        while True:
            user_item=input("enter rock, paper, or scissors").strip().lower()
            if user_item in ("rock","paper","scissors"):
                  return user_item
            else:
                print("Invalid choice ,please choose rock, paper, or scissors ")
    def get_computer_item(self):
        computer_item= random.choice(["rock","paper","scissors"])
        return computer_item
    def get_game_result(self, user_item, computer_item):
       if user_item==computer_item:
           return "draw"
       if (user_item=="paper" and computer_item=="rock") or (user_item=="scissors"and computer_item=="paper")or(user_item=="rock"and computer_item=="scissors"):
           return "win"
       else:
           return "loss"
    def play(self):
        user=self.get_user_item()
        computer=self.get_computer_item()
        result=self.get_game_result(user,computer)
        print(f"You selected {user}. The computer selected {computer}. You {result}")
        return result
    


      