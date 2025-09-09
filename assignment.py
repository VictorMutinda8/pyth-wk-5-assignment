# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"Device: {self.brand} {self.model}"


# Derived class (inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # call parent constructor
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self, percent):
        self.battery = min(100, self.battery + percent)
        print(f"Battery charged to {self.battery}%")

    def phone_info(self):
        return f"{self.device_info()} | Storage: {self.storage}GB | Battery: {self.battery}%"


# Example usage for Assignment 1
print("=== Assignment 1: Smartphone Class ===")
phone1 = Smartphone("Apple", "iPhone 14", 128, 80)
print(phone1.phone_info())
phone1.make_call("+254703814000")
phone1.charge(15)

print("\n")  # spacing


# =====================================
# Activity 2: Polymorphism Challenge 🎭
# =====================================

class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")


class Dog(Animal):
    def move(self):
        print("Running 🐕")


class Bird(Animal):
    def move(self):
        print("Flying 🐦")


class Fish(Animal):
    def move(self):
        print("Swimming 🐠")


# Example usage for Activity 2
print("=== Activity 2: Polymorphism Challenge ===")
animals = [Dog(), Bird(), Fish()]

for a in animals:
    a.move()
