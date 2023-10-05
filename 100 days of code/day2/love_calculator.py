name1 = input("What's the firts name?")
name2 = input("What's the second name?")
count =0
names_combined = name1 + name2
names_combined_lower = names_combined.lower()
t = names_combined_lower.count("t")
r = names_combined_lower.count("r")
u = names_combined_lower.count("u")
e = names_combined_lower.count("e")
count += (t+r+u+e)*10

l = names_combined_lower.count("l")
o = names_combined_lower.count("o")
v = names_combined_lower.count("v")
count += l + o + v +e

if count <10 or count>90:
    print(f"your score is {count}, you go together like coke and mentos")
elif count>40 and count<50:
    print(f"your score is {count}, you are alright together")
else:
    print(f"your score is {count}")
