numbers = [1, 1, 3, 5, 8, 12, 13, 21, 34, 55]
square_numbers = [square * square for square in numbers]
print(square_numbers)

list_of_strings = input().split(',')
numbers = [int(x) for x in list_of_strings]

result = [num for num in numbers if num % 2 == 0]

print(result)

sentence = input()
result = {word: print(word) for word in sentence.split()}

print(result)
