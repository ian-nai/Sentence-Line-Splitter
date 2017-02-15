import nltk
from nltk.tokenize import sent_tokenize
import random
import codecs
import os
import sys

print "Welcome! Please enter the names of the text files you'd like to import in the format [filename].txt"

text1 = raw_input("First filename: ")
text2 = raw_input("Second filename: ")
text3 = raw_input("Third filename: ")
text4 = raw_input("Fourth filename: ")

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

text_one = codecs.open(text1, "r", "utf-8")
text_two = codecs.open(text2, "r", "utf-8")
text_three = codecs.open(text3, "r", "utf-8")
text_four = codecs.open(text4, "r", "utf-8")

data = text_one.read()
data2 = text_two.read()
data3 = text_three.read()
data4 = text_four.read()

sent_tokenize_1 = sent_tokenize(data)
sent_tokenize_2 = sent_tokenize(data2)
sent_tokenize_3 = sent_tokenize(data3)
sent_tokenize_4 = sent_tokenize(data4)

len(sent_tokenize_1)
len(sent_tokenize_2)
len(sent_tokenize_3)
len(sent_tokenize_4)

rand_sent1 = random.choice(sent_tokenize_1)
rand_sent2 = random.choice(sent_tokenize_2)
rand_sent3 = random.choice(sent_tokenize_3)
rand_sent4 = random.choice(sent_tokenize_4)

print rand_sent1
print rand_sent2
print rand_sent3
print rand_sent4

start_over = raw_input("Would you like to run the program again? Type 'y' for yes and 'n' for no.")
if start_over == "y":
    os.execl(sys.executable, sys.executable, *sys.argv)
if start_over == "n":
    print "Bye!"
    exit(0)
else: 
    print("Please enter a valid input.")
