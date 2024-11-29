# address_space.py
class GPIBAddressSpace:
    def __init__(self, size=256):
        self.size = size
        self.memory = [0] * self.size

    def read(self, address):
        return self.memory[address]

    def write(self, address, data):
        self.memory[address] = data
