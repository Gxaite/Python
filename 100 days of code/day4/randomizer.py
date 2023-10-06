'''
Make a program that choice a person randomly
'''

import random

string_names = input("DIgite os nomes separados por , :")
names = string_names.split(", ")

choice = random.randint(0,len(names)-1)
print(names[choice])