import random

class MyList:
    def __init__(self,letters):
        self.letters = letters

    def reversed_list(self):
        return list(reversed(self.letters))
    
    def sorted_list(self):
        return sorted(self.letters)
    
    def random_numbers(self):
        return [random.randint(1,100) for _ in range(len(self.letters))]
    
    
my_list = MyList(['d', 'a', 'c', 'b'])
print("Original:", my_list.letters)
print("Reversed:", my_list.reversed_list())
print("Sorted:", my_list.sorted_list())
print("Random numbers:", my_list.random_numbers())