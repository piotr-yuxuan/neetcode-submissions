class SmartDevice:
    def __init__(self, name: str):
        self._name = name
    
    @property
    def name(self):
        return self._name

# TODO: Implement the SmartLight class
class SmartLight(SmartDevice):
    def turn_on(self) -> None:
        print(f"{self.name} is turned on")

    def turn_off(self) -> None:
        print(f"{self.name} is turned off")


# Don't change the code below
device = SmartLight("Smart Light")
device.turn_on()
device.turn_off()
