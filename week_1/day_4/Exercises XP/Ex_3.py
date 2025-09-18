from Ex_2 import Dog 
import random

class PetDog(Dog):
    def __init__(self, name, age, weight,trained=False):
        super().__init__(name, age, weight)
        self.trained=trained
  
       
    def train(self):
         print(self.bark())
         self.trained=True
    def play(self,*args):
        names= ",".join(dog.name for dog in args)
        print(f"{self.name},{names} All dogs play together")
    def do_a_trick(self):
       
        if self.trained:
            rand=random.randint(1,4)
            if rand == 1:
                print(f"{self.name} does a barrel roll")
            elif rand==2 :
                print(f"{self.name} stands on his back legs")
            elif rand ==3:
                print(f"{self.name}  shakes your hand")
            else:
                print(f"{self.name}  plays dead")
        

pet1=PetDog("rick",2,15)
pet2=PetDog("Chark",3,17)
pet3=PetDog("Doni",4,12,True)
print(pet1.trained)
pet1.train()
print(pet1.trained)
pet1.play(pet3,pet2)
pet3.do_a_trick()


