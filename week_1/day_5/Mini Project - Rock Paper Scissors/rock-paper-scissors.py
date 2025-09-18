def get_user_menu_choice():
    print("menu choice")
    print(""" 
           1 - Play a new game
           2 - Show scores
           x - Quit
    """)
    choice= input("choose an option :").strip().lower()

    if choice not in ("1","2","x"):
         print("Invalid choice. Please try again.")
         return None
    return choice
from game import Game
def main():
     results={"win":0,"draw":0,"loss":0}
     while True:
          choice= get_user_menu_choice()
          if choice is None:
               continue
          elif choice=="1" :
               
               game=Game()
               result = game.play()
               results[result]+=1
          elif choice =="2" :
               print_results(results)
          elif choice == "x":
               print_results(results)
               print("Thanks for playing! Goodbye")
               break
          
def print_results(results):
    print("\n=== Game Summary ===")
    print(f"Wins: {results['win']}")
    print(f"Draws: {results['draw']}")
    print(f"Losses: {results['loss']}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()