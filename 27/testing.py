

while True:
    a = input("Vlož číslo: ")
    try:
        print(a+2)
    except:
        print("Není číslo")
        continue
