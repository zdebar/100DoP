# CHECKING FOR SUBSTRINGS

addresses = [
    "123 Elm Street",
    "531 Oak Street",
    "678 Maple Street"
]
street = "Elm Street"

# Brute force (don't do this)
for address in addresses:
    address_length = len(address)
    street_length = len(street)
    for index in range(address_length - street_length + 1):
        substring = address[index:street_length + index]
        if substring == street:
            print(address)

# The index method
for address in addresses:
    try:
        address.index(street)
        print(address)
    except ValueError:
        pass

# The find method
for address in addresses:
    if address.find(street) >= 0:
        print(address)

# The in keyword (fastest/preferred)
for address in addresses:
    if street in address:
        print(address)


