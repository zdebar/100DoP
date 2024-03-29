# Calculator

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+":add, "-":substract, "*":multiply, "/":divide}

num1 = float(input("What's the first number?: "))
while True:      
    for key in operations:
        print(key)
        
    symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))

    answer = operations[symbol](num1, num2)
    print(f"{num1} {symbol} {num2} = {answer}")

    if input("Continue with previous result(y/n)?: ").lower() != "y":
        break
    num1 = answer