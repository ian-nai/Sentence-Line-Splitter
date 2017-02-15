import nltk
from nltk.tokenize import LineTokenizer
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

ln_tokenize_1 = LineTokenizer(blanklines='discard').tokenize(data)
ln_tokenize_2 = LineTokenizer(blanklines='discard').tokenize(data2)
ln_tokenize_3 = LineTokenizer(blanklines='discard').tokenize(data3)
ln_tokenize_4 = LineTokenizer(blanklines='discard').tokenize(data4)

len(ln_tokenize_1)
len(ln_tokenize_2)
len(ln_tokenize_3)
len(ln_tokenize_4)

rand_ln1 = random.choice(ln_tokenize_1)
rand_ln2 = random.choice(ln_tokenize_2)
rand_ln3 = random.choice(ln_tokenize_3)
rand_ln4 = random.choice(ln_tokenize_4)

print rand_ln1
print rand_ln2
print rand_ln3
print rand_ln4

start_over = raw_input("Would you like to run the program again? Type 'y' for yes and 'n' for no.")
if start_over == "y":
    os.execl(sys.executable, sys.executable, *sys.argv)
if start_over == "n":
    print "Bye!"
    exit(0)
else: 
    print("Please enter a valid input.")
