# gpib_ram.py
class GPIBRAM:
    def __init__(self, size=256):
        self.memory = [0] * size

    def read(self, address):
        return self.memory[address]

    def write(self, address, data):
        self.memory[address] = data

    def reset(self):
        self.memory = [0] * len(self.memory)
        print("RAM reset")

