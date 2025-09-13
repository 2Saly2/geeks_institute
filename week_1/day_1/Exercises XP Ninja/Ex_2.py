longest_sentence = ""  

while True:
    sentence = input(" write the sentence without character  A ")

    
    if sentence.lower() == "stop":
        break

    if "A" in sentence or "a" in sentence:
        print("the sentence have the character A ")
    else:
        if len(sentence) > len(longest_sentence):
            longest_sentence = sentence
            print("congratulations this sentence is the longest one ", longest_sentence)
        else:
            print("great but is not the longest one")