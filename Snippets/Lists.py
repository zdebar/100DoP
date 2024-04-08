# GET LAST ITEMS

my_list = ['red', 'blue', 'green']

# Get the last item using iterable unpacking
first_item, *_, last_item = my_list



# ADD TWO LISTS

ethernet_devices = [1, [7], [2], [8374163], [84302738]]
usb_devices = [1, [7], [1], [2314567], [0]]

# The long way
all_devices = [
    ethernet_devices[0] + usb_devices[0],
    ethernet_devices[1] + usb_devices[1],
    ethernet_devices[2] + usb_devices[2],
    ethernet_devices[3] + usb_devices[3],
    ethernet_devices[4] + usb_devices[4]
]

# Some comprehension magic
all_devices = [x + y for x, y in zip(ethernet_devices, usb_devices)]

# Let's use maps
import operator 
all_devices = list(map(operator.add, ethernet_devices, usb_devices))

# We can't forget our favorite computation library
import numpy as np 
all_devices = np.add(ethernet_devices, usb_devices)





# CONVERT TWO LISTS INTO DICTIONARIES

column_names = ['id', 'color', 'style']
column_values = [1, 'red', 'bold']

# Convert two lists into a dictionary with zip and the dict constructor
name_to_value_dict = dict(zip(column_names, column_values))

# Convert two lists into a dictionary with a dictionary comprehension
name_to_value_dict = {key:value for key, value in zip(column_names, column_values)}

# Convert two lists into a dictionary with a loop
name_value_tuples = zip(column_names, column_values) 
name_to_value_dict = {} 
for key, value in name_value_tuples: 
    if key in name_to_value_dict: 
        pass # Insert logic for handling duplicate keys 
    else: 
        name_to_value_dict[key] = value




# SORTING

my_list = ["leaf", "cherry", "fish"]

# Brute force method using bubble sort
my_list = ["leaf", "cherry", "fish"]
size = len(my_list)
for i in range(size):
    for j in range(size):
        if my_list[i] < my_list[j]:
            temp = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = temp

# Generic list sort *fastest*
my_list.sort()

# Casefold list sort
my_list.sort(key=str.casefold)

# Generic list sorted
my_list = sorted(my_list) 

# Custom list sort using casefold (>= Python 3.3)
my_list = sorted(my_list, key=str.casefold) 

# Custom list sort using current locale 
import locale
from functools import cmp_to_key
my_list = sorted(my_list, key=cmp_to_key(locale.strcoll)) 
 
# Custom reverse list sort using casefold (>= Python 3.3)
my_list = sorted(my_list, key=str.casefold, reverse=True)