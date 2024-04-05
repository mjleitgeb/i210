class Car:

    count = 0


    def __init__(self, make, color):
       self.make = make
       self.color = color
       self.miles = 0
       Car.count += 1
    
    def __str__(self):
       reply = "\nCar instance: "
       reply += "\nMake: {}".format(self.make)
       reply += "\nColor: {}".format(self.color)
       reply += "\nMiles: {}".format(self.miles)
       reply += "\nTotal cars: " + str(Car.count)
       return reply

    

    def drive(self, miles_driven):
        try:
            miles_driven = float(miles_driven)
            
            if miles_driven >= 0:
                self.miles += miles_driven
            elif self.miles_driven < 0:
                print("Enter a positive value.")
            return self.miles
        except ValueError:
            print("That is not a valid value.")


if __name__ == "__main__":
   car1 = Car("Subaru", "white")
   car2 = Car("Toyota", "orange")
   car3 = Car("Ford", "blue")
   car1.drive(45.0)
   car2.drive(12.2)
   car2.drive(5.0)
   car3.drive(20.5)
   car3.drive(20.5)
   car3.drive(20.5)
   car3.drive(20.5)
   car3.drive(20.5)
   print(car1)
   print(car2)
   print(car3)
