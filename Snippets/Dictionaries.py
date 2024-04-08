from collections import Counter, defaultdict


# MERGING

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Using dictionary comprehension
merged_dict = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}




# INVERTING

# Use to invert dictionaries that have unique values
my_inverted_dict = dict(map(reversed, dict1.items()))

# Use to invert dictionaries that have unique values
my_inverted_dict = {value: key for key, value in dict1.items()}

# print(merged_dict)  # Output: {'a': 1, 'b': 5, 'c': 4}

my_inverted_dict = dict(map(reversed, dict1.items()))
print(my_inverted_dict)

# Use to invert dictionaries that have non-unique values

my_inverted_dict = defaultdict(list)
{my_inverted_dict[v].append(k) for k, v in dict1.items()}



# SORTING

csv_mapping_list = [
  {
    "Name": "Jeremy",
    "Age": 25,
    "Favorite Color": "Blue"
  },
  {
     "Name": "Ally",
     "Age": 41,
     "Favorite Color": "Magenta"
  },
  {
    "Name": "Jasmine",
    "Age": 29,
    "Favorite Color": "Aqua"
  }
]

# Custom sorting
size = len(csv_mapping_list)
for i in range(size):
    min_index = i
    for j in range(i + 1, size):
        if csv_mapping_list[min_index]["Age"] > csv_mapping_list[j]["Age"]:
            min_index = j
csv_mapping_list[i], csv_mapping_list[min_index] = csv_mapping_list[min_index], csv_mapping_list[i]

# List sorting function
csv_mapping_list.sort(key=lambda item: item.get("Age"))

# List sorting using itemgetter
from operator import itemgetter
f = itemgetter('Name')
csv_mapping_list.sort(key=f)

# Iterable sorted function
csv_mapping_list = sorted(csv_mapping_list, key=lambda item: item.get("Age"))