class Dog :
    def __init__(self,name ,height):
        self.name =name,
        self.height = height

    def bark(self):
        print (f"{self.name} goes woof !")
    def jump(self):
        print(f"{self.name} jumps {self.height*2 } cm high ")



marwa_dog = Dog("max",50)
print(f"marwa's dog is {marwa_dog.name} and is {marwa_dog.height} cm tall")
marwa_dog.bark()
marwa_dog.jump()

anas_dog = Dog("Rex",20)
print(f"anas's dog is {anas_dog.name} and is {anas_dog.height} cm tall")
anas_dog.bark()
anas_dog.jump()

if marwa_dog.height > anas_dog.height:
    print(f"The bigger dog is {marwa_dog.name}")
else:
    print(f"The bigger dog is {anas_dog.name}")