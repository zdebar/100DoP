# def check_data_type(input, data_type):
  
#     while True:
#         try:
           
#             break
#         except ValueError: 
#             print("Invalid format!")
#     return 2


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))

# tip = check_data_type(input("How much tip would you like to give? 10, 12, or 15? "), int)
while True:
    try:
        tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
        break
    except ValueError: 
        print("Has to be number!")
people = int(input("How many people to split the bill? "))
amount = "{:.2f}".format(((100+tip)/100)*bill/people, 2)
print (f"Each person should pay {amount}.")
