for i in range(1,101):
    print(f"{i} ", end="")
    if i % 3 == 0:
        print("Fizz", end="")
    if i % 5 == 0:
        print("Buzz", end="")
    print()
    
