# gpib_stream.py
from gpib_master import GPIBMaster
from gpib_slave import GPIBSlave

class GPIBStream:
    def __init__(self):
        self.master = GPIBMaster()
        self.slave = GPIBSlave()

    def send_data(self, data):
        self.master.initiate(data)
        received_data = self.slave.listen()
        print(f"Stream received: {received_data}")
