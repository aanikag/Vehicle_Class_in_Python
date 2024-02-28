#main.py

from vehiclePackage.VehicleClass import *

if __name__ == "__main__":
    #instantiate an object if type Vehicle
    myCorvette = Vehicle("Car",120) #Trigger a call to constructor
    myCorvette.printType() 
    
    #invoke the getter for maximum speed, store the return value in a variable
    max_speed = myCorvette.getSpeed()
    print(max_speed)
    
    #instantiate another Vehicle object, you can name it
    myBeemer = Vehicle("Car",240) #myBeember is an object of type Vehicle
    myBeemer.printType()
    
    #I want a list of 3 vehicles: Car, Boat, Spaceship
    #You can pick the names and properties
    #I want some friendly output to demo your work
    myVehicles = [Vehicle("Volvo", 150), 
                  Vehicle("Yacht", 30), 
                  Vehicle("Apollo 11", 4000)]
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getSpeed())
    