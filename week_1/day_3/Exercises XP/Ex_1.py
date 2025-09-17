class cat:
   
   def __init__(self,name, age):
      self.name = name ,
      self.age = age,
   
def big_age (cats) :
      return max(cats , key =lambda c: c.age )
   
cat1 = cat("mino",2)
cat2= cat("lily",1) 
cat3= cat("lo" , 3)
cats=[cat1,cat2,cat3]

oldcat= big_age(cats)
print(f"the oldest cat is {oldcat.name} and is {oldcat.age}")
      
       
