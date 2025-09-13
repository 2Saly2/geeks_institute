nmb_1 = int(input("write the 1st number"))
nmb_2 = int(input("write the 2nd number"))
nmb_3 = int(input("write the 3rd number"))
if nmb_1 > nmb_2:
    nmb =nmb_1
else :
    nmb = nmb_2
if nmb > nmb_3 :
        print (f"The greatest number is {nmb}")
else:
        print (f"The greatest number is {nmb_3}")
        
print(f"The greatest number is {max(nmb_1 , nmb_2 , nmb_3)}")
