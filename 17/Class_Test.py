class Car():
    def __init__(self, seats = 4) -> None:
        self.seats = seats
    
    def enter_race_mode(self):
        self.seats = 2

fiat = Car(5)
fiat.enter_race_mode()
print(fiat.seats)