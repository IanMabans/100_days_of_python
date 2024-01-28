# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #     print(temperature)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
# dat_dict = data.to_dict()
# print(dat_dict)
#
# temp_list = data["temp"].mean()
# print(temp_list)
#
# print(data["temp"].max())
#
# print(data.condition)
#
# # get data in row
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# # create data frame
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76,56,32]
# }
# data_f = pandas.DataFrame(data_dict)
# print(data_f)
# data_f.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240128.csv")
grey_squirrels_count= len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count= len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count= len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]

}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")