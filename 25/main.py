# import csv

# with open("25/weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)


import pandas

data = pandas.read_csv("25/weather_data.csv")
data_dict = data.to_dict()
temperatures = data["temp"].to_list()


# Calculations with Columns
# average_temperatures = data["temp"].mean()
# max_temperature = data["temp"].max()


# Get Data in Column
# print(data["temp"])
# print(data.temp)


# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.index == data["temp"].idxmax()])
# print(data[data.temp == data.temp.max()])


# Create Dataframe from scratch
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("new_data.csv")


# Loop through a rows of a data frama
for (index, row) in data.iterrows():
    print(row)


