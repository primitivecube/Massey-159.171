# Optional Problem - convert the words in a sentence from a number to text
#
# Using the function from problem 3 and 4, write a program that repeatedly lets the user input a sentence: so
#
# Sentence: I have 27 cats and 9 dogs
#
# is converted to:
#
# I have twenty seven cats and nine dogs.
#
# The program repeatedly asks for sentences until the user enters the empty string (i.e. just presses the <enter> key.

a_sentence = "I have 27 cats and 9 dogs"

def number_to_word_converter(sentence):
  '''Enter a sentence, and all stand-alone single numbers will be converted to words'''

  number_to_word_dict_zero_to_nine = {0:"zero", 1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
  number_to_word_dict_ten_to_ninety = {1:"ten", 2: "twenty", 3:"thirty", 4:"fourty", 5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
  split_sentence = sentence.split()
  new_sentence = []

  for word in split_sentence:
    new_number = ""
    try:
      if int(word) / 1 == int(word):
        if len(word) == 2:
          new_number += number_to_word_dict_ten_to_ninety[int(word[0])]
          if int(word[1]) != 0:
            new_number += "-" + number_to_word_dict_zero_to_nine[int(word[1])]
        elif len(word) == 1:
          new_number = number_to_word_dict_zero_to_nine[int((word))]
        new_sentence.append(new_number)
    except:
      new_sentence.append(word)

  return " ".join(new_sentence)


def number_to_word_requester():
    '''This program repeatedly asks for sentences until the user enters the empty string (i.e. just presses the <enter> key)'''
    while True:
        sentence_to_convert = input("Enter a sentence to convert (press <enter> to exit): ")
        print(number_to_word_converter(sentence_to_convert))
        if sentence_to_convert == "":
            return

number_to_word_requester()

# This is now working for stand alone numbers from 0-10, and 20-99.
# It could be improved with the following extensions:
# - handle teen numbers
# - handle more than two digit numbers
# - handle numbers that are separated by commars
# - handle numbers within words
