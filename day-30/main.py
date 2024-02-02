try:
    file = open('a_file.txt')
    a_dictionary = {'key': 'value'}
    print(a_dictionary['key'])
except FileNotFoundError:
    file = open('a_file.txt', 'w')
    file.write("Something went wrong")
except KeyError as error_message:
    print(f"That key {error_message} doesn't exist")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This error is serious")

# New code to catch exceptions
height = float(input('Height: '))
weight = float(input('Weight: '))

if height > 3:
    raise ValueError("Height must be less than 3")

bmi = weight / height ** 2
print(bmi)

fruits = eval(input())


def make_pie(index):
    try:
        fruit = fruits[index]

    except:
        print("Fruit Pie")
    else:
        print(fruit + 'pie')


make_pie(4)

