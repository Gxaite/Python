year = int(input("Check if is a leap year: "))
if year%4 ==0:
    if year%100 == 0:
        if year%400 ==0:
            print(f"{year} is a leap year")
            exit()  

        print(f"{year} ins't a leap year")
        exit()


    print(f"{year} is a leap year")
    