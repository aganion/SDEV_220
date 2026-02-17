"""
Alicia Ganion
2/16/2026
SDEV 220
"""

class Vehicle:
    def __init__(self, group):
        self.group = group

class Automobile(Vehicle):
    def __init__(self, group, year, make, model, doors, roof):
        super().__init__(group)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    def display_data(self):
        print("--Saved Car Data--")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Doors: {self.doors}")
        print(f"Roof: {self.roof}")

intro_app = print("Welcome to the vehicle data system.")
year = int(input("Enter year of car: "))
make = input("Enter make of vehicle: ")
model = input("Enter model of vehicle: ")

while True:
    doors = input("Enter doors of vehicle (2 or 4): ")
    if doors in ["2", "4"]:
        doors = int(doors)
        break
    print("Invalid entry. Please enter 2 or 4.")

while True:
    roof = input("Enter roof of vehicle (solid or sun roof): ").lower()
    if roof in ["solid", "sun roof"]:
        break
    print("Invalid entry. Please enter solid or sun roof.")

car_data = Automobile("Car", year, make, model, doors, roof)

car_data.display_data()

