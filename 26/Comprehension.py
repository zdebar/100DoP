# List comprehension test

# numbers = [ 1, 2, 3]
# new = [ n for n in numbers]
# print(new)

# name = "Angela"
# letter_list = [ n for n in name]
# print(letter_list)
# print("".join(letter_list))

# double = [n*2 for n in range(1,5)]
# print(double)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {i: j for i,j in weather_c.items()}

print(weather_f)