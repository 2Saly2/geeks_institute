def letter_position (word):
    word=word.strip().lower()
    positions = {}
    for index , letter in enumerate(word):
        if letter not in positions:
            positions[letter]=[index]
        else :
            positions[letter].append(index)
    return positions
def main ():
    user_word = input("enter a word")
    result = letter_position(user_word)
    print("dictionary :" ,result)


main()
    