# with open("./25/weather_data.csv") as weather_file:
#     data = weather_file.readlines()
#     print(data)

import csv
import pandas

# with open ("./25/weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = [int(row[1]) for row in data if row[1] != "temp"]
#     print(temperatures)
#     weather_file.seek(0)
#     for row in data:
#         print(row)

data = pandas.read_csv("./25/weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data["temp"].mean())
# print(data["temp"].max())

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp*9/5+32
# print(monday_temp_F)

# Create Dataframe from Scratch (from dictionary)
data_dict = {}
data = pandas.DataFrame(data_dict)
# Print to CSV file
data.to_csv("new_data.csv")