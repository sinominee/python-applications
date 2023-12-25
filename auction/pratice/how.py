programming_dictionary = {
    "Bug": "An error on a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    }

# retriveing
print(programming_dictionary["Bug"])

# # adding
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# # create empty dic
# empty_dictionary = {}

# # wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# # edit an item in the dictionary
# programming_dictionary["Bug"] = "An error on a program that prevent's the program from running as expected."
# print(programming_dictionary)

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
