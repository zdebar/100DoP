from collections import Counter

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# # Using dictionary comprehension
# merged_dict = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}

# print(merged_dict)  # Output: {'a': 1, 'b': 5, 'c': 4}

my_inverted_dict = dict(map(reversed, dict1.items()))
print(my_inverted_dict)