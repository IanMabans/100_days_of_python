with open(file="/home/mabans/Documents/my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("/home/mabans/Documents/my_file.txt", mode="a") as file:
    file.write("\n I am good")

with  open("joy.txt", mode="w") as file:
    file.write("new text")
