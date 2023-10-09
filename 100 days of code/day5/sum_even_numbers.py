number = int(input("Calculate even numbers from 0 to : "))
result = 0
for i in range(0,number+1,2):
    result += i
print(result)