#Number divisble by 5 or 7

number = int(input("enter the number:"))
if (number % 7 == 0) and (number % 5 == 0):
    print(f"The number{number} is divisible by 7 or 5")
else:
    print(f"The number{number} is not divisible")    



