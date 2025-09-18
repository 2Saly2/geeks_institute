from Ex_4 import Family
class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['name']} uses power: {member['power']}")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old!")

    def incredible_presentation(self):
        print("Here is our powerful family **")
        super().family_presentation()


members = [
    {'name':'Amal','age':20,'gender':'Female','is_child':False,'power':'read minds','incredible_name':'SuperWoman'},
    {'name':'Saaid','age':32,'gender':'Male','is_child':False,'power':'fly','incredible_name':'SaidFly'}
]

inc = TheIncredibles("Ait lahssaine", members)
inc.incredible_presentation()

inc.born(name="Ahmade", age=1, gender="Male", is_child=True, power="Unknown Power", incredible_name="BabyH")

inc.incredible_presentation()


inc.use_power("Saaid")   
