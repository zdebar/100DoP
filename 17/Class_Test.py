class Car:
    def __init__(self, seats = 4) -> None:
        self.seats = seats

fiat = Car(5)
print(fiat.seats)