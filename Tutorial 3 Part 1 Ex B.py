# i) Ask the user to enter a sentence. Using the string function split(),
# create a list where each word in the sentence is a new item in the list.
# e.g. if the user entered “Where the wild things are”, the list will look like ['Where', 'the', 'wild', 'things', 'are']
# ii) Use a for loop to go through each item in your list and use the string function upper()
# to print each string in UPPER case.

def split_sentence():
    sentence = input("Enter a sentence: ")
    list = sentence.split()
    return list

print(split_sentence())

def sentence_upper(list):
    for i in list:
        word = i.upper()
        print(word)

sentence_upper(split_sentence())

# Try using other string functions e.g. lower(), title(), capitalize(), replace(<this>, <that>)

def sentence_lower():
    for i in split_sentence():
        word = i.lower()
        print (word)

sentence_lower()

def title():
    for i in split_sentence():
        print (i.title())

title()

def capitalize():
    for i in split_sentence():
        print (i.capitalize())

capitalize()

def replace():
    for i in split_sentence():
        print (i.replace("W", "x"))

replace()
