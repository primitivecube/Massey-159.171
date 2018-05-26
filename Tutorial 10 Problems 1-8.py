# Problem 1: Display the fields from a dictionary

# Display the value for each of 'title', 'cost' and 'brand' in the following dictionary,
#
# item = {'title':'Toaster', 'cost':'79.95', 'brand': 'Vogels' }
#
# print(item.values())

# Problem 2 - display all of a dictionary's key and values
#
# Using a for-loop, display each name-value pair in the item dictionary on a new line.
#
# There will be only one print statement.

# for key, values in item.items():
#     print(key, values)

# Problem 3 - Updating values in a dictionary
#
# Modify the cost of the toaster to '49.95' by updating the 'cost' in the item dictionary,
#
# Then display the updated values of the name-value pairs, using the for-loop from Problem 2.

# item['cost'] = '49.95'
#
# for key, values in item.items():
#     print(key, values)

# Problem 4: Write a function that creates dictionary entries
#
# This function prompts for a item title and its cost and then creates a two element dictionary, with keys 'title' and 'cost' (as shown in Problem 1). If the user enters quit for the item title, immediate exit from the function and return None instead of a dictionary.
#
# Leave the costs as strings - i.e. don't convert them to floats (you'll do that later).
#
# The main program repeated calls the function and does two things with the returned dictionary:
#
# prints it directly (as in the second line here):
# details = getDetails()
# print("The dict returned was : ", details)
# then prints the title and cost formatted so they appear in a sentence
# e.g.
#
# The Toaster was $79.95
# It stops calling the function when None is returned by the function instead of a dictionary.

# def dict_update():
#     dict = {'title':None, 'cost':None}
#     title_value = input("Enter a title: ")
#     if title_value.lower() == 'quit':
#         return None
#     cost_value = input("Enter the cost ($): ")
#     dict['title'] = title_value
#     dict['cost'] = cost_value
#     return dict

# while True:
#     update = dict_update()
#     if update == None:
#         break
#     else:
#         print("The dict returned was : {}".format(update))
#         print("The {} was ${}".format(update['title'],update['cost']))

# Problem 5 - Adding the returned values to a list
#
# Call the function given in Problem 4, but instead of just printing the values when the function returns, add the returned dictionary to a list.
#
# If you print your list, it should look like:
#
# print(items)
#
# [ {'title':'Toaster', 'cost':'79.95'},
#   {'title':'Bread', 'cost':'3.75'},
#   {'title':'Peas', 'cost':'2.50'}    ]
# except that it'll probably all be on one line.
#
# When the user enters quit, display all the entries in the list of dictionaries in the order they were entered.
#
# i.e. use for item in yourListOfDictionaries …
#
# Remember that item will be a dictionary.

# list_of_dicts = []
#
# while True:
#     update = dict_update()
#     if update is not None:
#         list_of_dicts.append(update)
#     if update is None:
#         print(list_of_dicts)
#         break

# Problem 6 - write a function that can modify dictionary entries
#
# Write a function fixCosts(d) where the parameter d is a dictionary of items. The function changes the cost field of each entry from a string to a number.
#
# If your dictionary was called items:
#
# Before calling fixCosts(), print(items) would look like:
#
# [ {'title':'Toaster', 'cost':'79.95'},
#   {'title':'Bread', 'cost':'3.75'},
#   {'title':'Peas', 'cost':'2.50'}    ]
# After calling fixCosts(), print(items) would display:
#
# [ {'title':'Toaster', 'cost': 79.95},
#   {'title':'Bread', 'cost': 3.75},
#   {'title':'Peas', 'cost': 2.50}    ]
# Note the costs are now numbers.
#
# Calculate the total cost of all the items.
#
# def fixCosts(d):
#     for dictionary in d:
#         try:
#             dictionary['cost'] = float(dictionary['cost'])
#         except:
#             print("The cost entry {} is not a number".format(dictionary['cost']))
#
# d = [{'title': 'Toaster', 'cost': '79.95'},{'title':'Bread', 'cost':'3.75'}]
# print(d)
# fixCosts(d)
# print(d)
# total_costs = 0
# for dict in d:
#     total_costs += dict['cost']
# print(total_costs)

# Problem 7- Adding the returned dictionaries to a dictionary
#
# Instead of adding the dictionary returned by your function to a list, now add the returned dictionary to another dictionary (called maybe itemdict).
#
# The keys of values in the new dictionary could be either:
#
# the sequence number of the items. For example if you entered the items as displayed above,
#
# print(itemdict)
#
# { 1: {'title':'Toaster', 'cost': '79.95'},
#   2: {'title':'Bread', 'cost': '3.75'},
#   3: {'title':'Peas', 'cost': '2.50'} }
# OR
#
# you could create the new dictionary using the returned title's value as the key:
#
# print(itemdict)
#
# { 'Toaster': {'title':'Toaster', 'cost': '79.95'},
#   'Bread'  : {'title':'Bread', 'cost': '3.75'},
#   'Peas'   : {'title':'Peas', 'cost': '2.50'} }

# def dict_update():
#     dict = {'title':None, 'cost':None}
#     title_value = input("Enter a title: ")
#     if title_value.lower() == 'quit':
#         return None
#     cost_value = input("Enter the cost ($): ")
#     dict['title'] = title_value
#     dict['cost'] = cost_value
#     return dict

# itemdict = {}

# while True:
#     update = dict_update()
#     if update is not None:
#         itemdict[update['title']] = update
#     if update is None:
#         print(itemdict)
#         break

# Problem 8 - Display the items sorted by title (harder)
#
# Display the items in the list sorted alphabetically on the title. For this, you'll have to get the list of titles (i.e. the dictionary's keys), turn them into a list (using the list() function), sort them and then use these to access the cost.
#
# It's much easier if you use the second form of dictionary shown in the previous problem.

def dict_update():
    dict = {'title':None, 'cost':None}
    title_value = input("Enter a title: ")
    if title_value.lower() == 'quit':
        return None
    cost_value = input("Enter the cost ($): ")
    dict['title'] = title_value
    dict['cost'] = cost_value
    return dict

itemdict = {}

while True:
    update = dict_update()
    if update is not None:
        itemdict[update['title']] = update
    if update is None:
        for key in sorted(itemdict):
            print(itemdict[key])
        break
