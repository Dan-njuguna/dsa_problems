#!/usr/bin/python3

class Vehicle:
    def __init__(self):
        self.max_speed = 0
        self.mileage = 0
        self.color = "White"
    
    def show_info(self):
        print("Vehicle info:")
        print("\t-- Max speed:", self.max_speed)
        print("\t-- Mileage:", self.mileage)
        print("\t-- Color:", self.color)


gari = Vehicle()
gari.max_speed = 240
gari.mileage = 10000
gari.show_info()


class Bus(Vehicle):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.seating_capacity = 50
        self.color = "White"
    
    def show_info(self):
        print("Bus info:")
        print("\t-- Name:", self.name)
        print("\t-- Seating Capacity: ", self.seating_capacity)
        super().show_info()

forest = Bus()
forest.name = "Glorious"
forest.max_speed = 140
forest.mileage = 300000
forest.show_info()


upperLimit = 100
for i in range(0, upperLimit + 1):
    print(i, end=" ")
    if i == 100:
        print("")
print()

for i in range(0, upperLimit + 1):
    if i % 7 == 0:
        print(i, end=" ")
print()

for i in range(0, upperLimit + 1):
    if i % 5 == 0 and not i % 3 == 0:
        print(i, end=" ")
print()

for x in range(2, 21):
    divisors = [i for i in range(2, x) if x % i == 0]  # Find divisors excluding 1 and x
    if divisors:
        print(f"{x}: {' '.join(map(str, divisors))}")

def polynomial(a: int, b: int = 0, c: int = 0, x: int = 3):
    return a * x ** 2 + b * x + c

print("3x2 - x + 2 = ", polynomial(3, -1, 2))