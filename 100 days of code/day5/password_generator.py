import random

password = ""

symbols = ['!','@','#','$','%','¨&','*','+','(',')']
numbers = ['1','2','3','4','5','6','7','8','9','0']
upper_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','W']
lower_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','w']

symbols_count = int(input("Number of symbols: "))
numbers_count = int(input("Number of numbers: "))
upper_letters_count = int(input("Number of Upper letters: "))
lower_letters_count = int(input("Number of Lower letters: "))

for i in range(0,symbols_count):
    password += str(symbols[random.randint(0,symbols_count)])

for i in range(0,numbers_count):
    password += str(numbers[random.randint(0,numbers_count)])

for i in range(0,upper_letters_count):
    password += str(upper_letters[random.randint(0,upper_letters_count)])

for i in range(0,lower_letters_count):
    password += str(lower_letters[random.randint(0,lower_letters_count)])


print (password)