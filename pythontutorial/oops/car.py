class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15 # 15%
        else:
            self.tax = 0.12 # 12%
       # self.display_all()

    def display_all(self):
        print ("Price: ${}".format(self.price))
        print ("Speed: {} mph".format(self.speed))
        print ("Fuel:", self.fuel)
        print ("Mileage: {} mpg".format(self.mileage))
        print ("Tax: {}%".format(int(self.tax * 100)))

print ("Car 1: ")
mycar = Car(20000, 35, 'Petrol', 15)
mycar.display_all()
myfriendcar = Car(30000, 30, 'Electric', 100)
'''
print ("Car 2: ")
car2 = Car(2000, 5, 'Electric', 105)
print ("Car 3: ")
car3 = Car(2000, 15, 'Diesel', 95)
print ("Car 4: ")
car4 = Car(2000, 25, 'Hybrid', 25)
print ("Car 5: ")
car5 = Car(2000, 45, 'Petrol', 25)
print ("Car 6: ")
car6 = Car(20000000, 35, 'Petrol', 15)
'''