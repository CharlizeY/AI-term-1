first_num = int(input("Please enter the first integer: "))
second_num = int(input("Please enter the second integer: "))
if first_num >= second_num:
    print(first_num)
else:
    print(second_num)



first_num = int(input("Please enter the first integer: "))
second_num = int(input("Please enter the second integer: "))
third_num = int(input("Please enter the third integer: "))
if first_num >= second_num and first_num >= third_num:
    print(first_num)
elif second_num >= first_num and second_num >= third_num:
    print(second_num)
else:
    print(third_num)



year = int(input("Please enter a year: "))
if year % 4 == 0 and year % 100 !==0:
    print("Leap year")
elif year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")



temp = float(input("Please enter temperature: "))
if temp < 20:
    print("Too cold")
    print(f"New temperature: {temp+1}")
elif temp > 22:
    print("Too hot")
    print(f"New temperature: {temp-1}")
else:
    print("Just nice!")
    print(f"New temperature: {temp}")

    

