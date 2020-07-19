num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
sum = float(num1) + float(num2)
if sum > 10:
    print(str(sum) + " is greater than 10!")
elif sum < 10:
    print(str(sum) + " is less than 10!")
else:
    print("Your number is 10!")
