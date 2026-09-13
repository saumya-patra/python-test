class robot_dog:
    def __init__(self, name):
        self.name = name
        self.battery_level = 100

    def bark(self):
        if self.battery_level > 0:
            print(f"{self.name} says: Woof!")
            self.battery_level -= 10
        else:
            print(f"{self.name} is out of battery!")

    def charge(self):
        self.battery_level = 100
        print(f"{self.name} is fully charged!")

    def status(self):
        print(f"{self.name}'s battery level: {self.battery_level}%")
# Main program
my_dog = robot_dog("Rex")
my_dog.status()