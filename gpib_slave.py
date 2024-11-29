# gpib_slave.py
from gpib_channels import GPIBChannel

class GPIBSlave:
    def __init__(self):
        self.channel = GPIBChannel()

    def listen(self):
        if self.channel.dav == 1:
            command = self.channel.data
            print(f"Slave received command: {hex(command)}")
            return command
        return None

    def reset(self):
        self.channel.clear()
        print("Slave reset")
