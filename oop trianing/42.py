class Motorcycle:
    def __init__(self):
        self.speed = 0
        self.mileage = 0

    def start(self):
        return "Motorcycle is starting..."
    
    def accelerate(self, amount):
        self.speed += amount
        return f"Accelerating... Current speed: {self.speed} km/h"

    def add_mileage(self, distance):
        self.mileage += distance

    def stop(self):
        self.speed = 0
        return "Motorcycle has stopped."
    
    def get_status(self):
        return f"Current Speed: {self.speed} km/h, Total Mileage: {self.mileage} km"
    
bike = Motorcycle()

while True:
    command = input("Enter command:").lower().split()
    if command[0] == "start":
        print(bike.start())

    elif command[0] == "accel":
        if len(command) > 1 and int(command[1]) > 0:
            print(bike.accelerate(int(command[1])))

        else:
            print("Invalid command. Please try again.")

    elif command[0] == "mileage":
        if len(command) > 1 and int(command[1]) > 0:
            bike.add_mileage(int(command[1]))

        else:
            print("Invalid command. Please try again.")

    elif command[0] == "stop":
        print(bike.stop())

    elif command[0] == "status":
        print(bike.get_status())

    elif command[0] == "exit":
        print("Goodbye.")
        break

    else:
        print("Invalid command. Please try again.")
