#a system to track different types of robots in a warehouse.
class Robot:
    #class attribute
    manufacturer_name =  "Riotlabs"
    #instance attribute 
    def __init__(self, name, serial_number, battery_level= 100):
        self.name = name
        self.serial_number = serial_number
        self.battery_level = battery_level
    
    def work_hours(self, hour_worked):
        #for every work hour, battery level minus 10
        for every_hour in range(hour_worked):
            self.battery_level -= 10
        print(f"current bot battery level {self.battery_level}")

    def __str__(self):
        return f'{self.name} | SN: [{self.serial_number}] | Battery: [{self.battery_level}]%'

# drone_bot = Robot("drone_bot", 1122, 100)
# print(drone_bot)

#child class
class drone_robot(Robot):
    #new attribute
    def __init__(self,name, serial_number, flight_altitude_limit):
        super().__init__(name, serial_number)
        self.flight_altitude_limit =flight_altitude_limit
    
    def work_hours(self, hour_worked):
        for every_hour in range(hour_worked):
            self.battery_level -= 20
        print(f"current bot battery level {self.battery_level}")

    def fly(self, altitude):
        
        print(f"{self.name} is now airbone at {altitude} meters")

class clean_robot(Robot):
    #new attribute
    def __init__(self, dust_bin_capacity):
        self.dust_bin_capacity =dust_bin_capacity 

    def empty_bin(self):
        print(f"cleaning bin ... Done!!")

#basic bot
bot = Robot("Generic-01", "SN100")
print(bot)
bot.work_hours(2)
print(bot)

#create drone
flyer = drone_robot("SkySpy", "SN500", 120)
flyer.fly("20")
# flyer.work_hours(1)