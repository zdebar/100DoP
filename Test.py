class Car:
    def __init__(self, speed):
        self.__speed = speed  # Speed is encapsulated

    def get_speed(self):
        return self.__speed  # Accessor method for speed

    def set_speed(self, speed):
        if speed < 0:
            raise ValueError("Speed cannot be negative")
        self.__speed = speed  # Mutator method for speed

car = Car(100)
print(car.get_speed())  # Output: 100

# Attempt to access speed directly raises an AttributeError
print(car.__speed)  # This will raise an AttributeError

# Attempt to set negative speed raises a ValueError
car.set_speed(-50)  # This will raise a ValueError
