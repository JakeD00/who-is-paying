import random
import os

# Split string method
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
random_name = random.randint(0,len(names)-1)
print(f"{names[random_name]} is going to buy the meal today!")
os.system('pause')