# # Check if a user can use a rollercoaster and check the prices accordingly
# import sys
# bill = 0
# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm?"))

# if height < 120:
#     print("You can't ride the rollercoaster")
#     sys.exit()

# print("You can ride the rollercoaster")
# age = int(input("What is your age? "))

# if age >= 18:
#     print("Pay 185")
#     bill = 185
# elif age < 12:
#     bill = 100
#     print("Pay 100")
# elif 12 <= age <= 18:
#     print("Pay 130")
#     bill = 130
# wants_photo = input("Do you want a photo? Y or N. ")
# if wants_photo == "Y":
#     bill += 50
# print(f"Your final bill is {bill}")


    
    
# #  Check whether number is even or odd   # 
# num = int (input("Input your number: "))
# if num %2 == 0 :
#     print ("Your number is even")
# else :
#     print("Your number is odd")  

# # Check your bmi
# height = float(input())
# weight = float(input())
# bmi = weight / (height * height)
# if bmi < 18.5:
#     print(f"Your bmi is {bmi}, you are underweight")
# elif bmi < 25:
#     print(f"Your bmi is {bmi}, you are normal weight")
# elif bmi <30:
#     print(f"Your bmi is {bmi}, you are slightly overweight")
# elif bmi <35:
#     print(f"Your bmi is {bmi}, you are obese")        
# else:
#     print(f"Your bmi is {bmi}, you are clinically obese")

# #  check if year is leap year
# year = int(input("Please enter a year"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"Year {year} is leap year")
#         else:
#             print(f"Year {year} is not a leap year")
#     else:
#         print(f"Year {year} is a leap year")
# else:
#     print(f"Year {year} is not a leap year")

print("Thank you for choosing pizza delivery service")
size = input("Enter size of pizza. S or M or L")
add_pepperoni = input("Do you want to add pepperoni? (y/n): ")
extra_cheese = input("Do you want to add extra cheese? (y/n): ")    
bill = 0
if size =="S":
    bill +=15
elif size =="M":
    bill +=20
else :
    bill += 25
    
if add_pepperoni == "Y":
    if size == "S":
        bill +=2
    if size == "M":
        bill += 3
    if size == "L":
        bill += 5

if extra_cheese == "Y":
    bill += 2

print(f"Your final bill is : $ {bill} ")

    