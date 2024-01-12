# For Loop
fruits = ["Apple", "Peach", "Pears"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")
print(fruits)
# input a python list of students heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
    total_height += height
print(f"Total height = {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students +=1
print(f"Number of students = {number_of_students}")

average_heights = round(total_height/number_of_students)
print(f"Average heights = {average_heights}")

# High Score
# Input Students Scores
student_scores = input("Enter the student scores and separate them with spaces").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"Highest Score = {highest_score}")

# for loop with range
for number in range(1, 11, 3):
    print(number)
total = 0
for number in range(1, 101):
    total += number
print(total)

# Sum of even numbers between 0 and 1000
target = int(input("Enter even number\n"))
even_sum = 0
for number in range(2, target+1, 2):
    even_sum += number
print(even_sum)

# fizz Buzz
target = 100
for number in range(1, target+1, 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
for char in range(1, nr_symbols+1):
    password += random.choice(symbols)
print(password)
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
print(password_list)
random.shuffle(password_list)
print(password_list)
pasword = ""
for char in password_list:
    pasword += char
print(f"Your password is {pasword}")
