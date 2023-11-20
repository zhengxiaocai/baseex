class Lamp:
    def __init__(self, color):
        self.color = color
        self.on = False

    def state(self):
        return f'The lamp is {"on" if self.on else "off"}.'

    def toggle_switch(self):
        self.on = not self.on


if __name__ == '__main__':
    my_lamp = Lamp("Blue")

    print(my_lamp.color == "Blue")
    print(my_lamp.on is False)
    print(my_lamp.state() == "The lamp is off.")

    my_lamp.toggle_switch()
    print(my_lamp.state() == "The lamp is on.")

    my_lamp.toggle_switch()
    print(my_lamp.state() == "The lamp is off.")
