user_word = input("write a word")
result =""
previous =""


for c in user_word :
    if c != previous :
        result+= c
        previous = c
print(f"result : {result}")