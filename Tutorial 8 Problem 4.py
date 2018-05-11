# Problem 4 - Extend the number-to-word converter to handle values 1-100
#
# This is the same as the previous problem and can convert values from any value from 1-100 apart from 10-19.
# Adding these is easy but it's just more typing.
#
# so
#
# print( toWord(39) ) displays thirty nine
# print( toWord(20) ) displays twenty
# print( toWord(55) ) displays fifty five
# Use lists to implement this solution, and do it in two stages.

def toWord(number):
    list_one_to_nine = ['one','two','three','four','five','six','seven','eight','nine']
    list_20_to_100 = ['twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
    number_of_digits = len(str(number))
    if number_of_digits == 3:
        return 'one hundred'
    elif number_of_digits == 2:
        first_number = number  // 10
        second_number = number % 10
        if second_number == 0:
            return list_20_to_100[first_number-2]
        else:
            return '{} {}'.format(list_20_to_100[first_number-2],list_one_to_nine[second_number-1])
    elif number_of_digits == 1:
        return list_one_to_nine[number-1]

for number in [100,20,55]:
    print( toWord(number))
