class DeskLamp:
    instance = None

    def __init__(self, is_on=False, brightness=5, color="white", producer="Unknown"):
        self.is_on = is_on
        self.brightness = brightness
        self.color = color
        self.producer = producer

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_off = False

    @staticmethod
    def get_instance():
        if not DeskLamp.instance:
            DeskLamp.instance = DeskLamp()
        return DeskLamp.instance
    def __str__(self):
        return f"Is_on: {self.is_on}\nBrightness: {self.brightness}\nColor: {self.color}\nProducer: {self.producer}\n"

if __name__ == "__main__":
    lamps1 = DeskLamp()
    lamps2 = DeskLamp(True, 8, "red", "Producer1")
    lamps3 = DeskLamp.get_instance()
    lamps4 = DeskLamp.get_instance()

    lamps = [lamps1, lamps2, lamps3, lamps4]
    for lamp in lamps:
        print(lamp)
    

    
    
