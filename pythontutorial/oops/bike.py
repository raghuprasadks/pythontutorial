class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print ("Bike's Price: ${}".format(self.price))
        print ("Bike Maximum Speed: {} mph".format(self.max_speed))
        print ("Total Miles Ridden: {} miles".format(self.miles))
        return self

    def ride(self):
        print ("Riding...")
        self.miles += 10
        return self

    def reverse(self):
        if self.miles < 6:
            print ("Cannot reverse bike that hasn't been ridden forward")
        else:
            self.miles -= 5
            print ("Reversing")
        return self

bike1 = Bike(5000, 250)
bike2 = Bike(500, 35)
bike3 = Bike(50, 2)

print ("Bike 1")
bike1.ride().ride().ride().reverse().displayInfo()
print ("Bike 2")
bike2.ride().ride().reverse().reverse().displayInfo()
print ("Bike 3")
bike3.reverse().reverse().reverse().displayInfo()