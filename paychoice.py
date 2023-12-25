import random

names_string = input("Give me everybody's names, seperated by a comma.\n")
names = names_string.split(", ")
# num_items = len(names)
# r_name = random.randint(0, num_items - 1)
# final_name = names[r_name]
# print("who pays for food is " + final_name)

person_choice = random.choice(names)
print(person_choice + " is gonna pay")