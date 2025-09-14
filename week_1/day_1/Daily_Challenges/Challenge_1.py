number = int(input("write a int number"))
length = int (input("write a int length"))

if length <= 0 :
    result = []
else:
    result = []
    for i in range(1 , length+1):
       result.append(number * i)
       
print(f"list of multiples :{result}")