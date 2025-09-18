class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations! {kwargs['name']} was born into the {self.last_name} family!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Family last name: {self.last_name}")
        print("Members:")
        for member in self.members:
            print(member)

members = [
    {'name':'Amal','age':20,'gender':'Female','is_child':False},
    {'name':'Saaid','age':32,'gender':'Male','is_child':False}
]

fam = Family("Ait lahssaine", members)
fam.family_presentation()
fam.born(name="Nouhaila", age=0, gender="Female", is_child=True)
print(fam.is_18("Amal"))  
print(fam.is_18("Taha"))    
fam.family_presentation()