# gpib_master.py
from gpib_channels import GPIBChannel

class GPIBMaster:
    def __init__(self):
        self.channel = GPIBChannel()

    def initiate(self, command):
        self.channel.dav = 1
        self.channel.data = command
        print(f"Master sending command: {hex(command)}")
        self.channel.dav = 0

    def reset(self):
        self.channel.clear()
        print("Master reset")
