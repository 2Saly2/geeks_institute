class Dog :
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight

    def bark(self):
        return f'{self.name} is barking '
    def run_speed(self):
        return  self.weight/self.age*10
    def fight(self,other_dog):
       if self.run_speed()*self.weight > other_dog.run_speed() * other_dog.weight:
           return self.name 
       else :
           return other_dog.name
       
dog1 = Dog("dodo",2,15)
dog2 =Dog("bobo",5,16)
dog3=Dog("dib",1,15)
print(dog1.bark())
print(dog1.run_speed())
print(dog1.fight(dog3))