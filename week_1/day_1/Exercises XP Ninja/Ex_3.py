paragraph = """You'll find interesting articles to read on topics like making better decisions, accelerating learning, and more.
 You'll also find articles explaining how to use mental models, how to read better, and finding your purpose.
 Ready to dive in? You can start with my greatest hits or scroll down to see every article by month and title."""


characters = len(paragraph)
import re
sentences = re.split(r'[.!?]', paragraph)
sentences = [s.strip() for s in sentences if s.strip() != ""]
sentence_count = len(sentences)
words = paragraph.split()
word_count = len(words)

unique_words = set(words)
unique_count = len(unique_words)


non_space_characters = len(paragraph.replace(" ", ""))
average_words_per_sentence = word_count / sentence_count
non_unique_count = word_count - unique_count

print("characters :", characters)
print("sentences:", sentence_count)
print("words :", word_count)
print("unique words :", unique_count)
print("non-whitespace :", non_space_characters)
print("average amount of words :", average_words_per_sentence)
print(" amount of non-unique words :", non_unique_count)