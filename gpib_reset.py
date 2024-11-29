# gpib_reset.py
from gpib_master import GPIBMaster
from gpib_slave import GPIBSlave

class GPIBReset:
    def __init__(self):
        self.master = GPIBMaster()
        self.slave = GPIBSlave()

    def reset_all(self):
        self.master.reset()
        self.slave.reset()
        print("GPIB system reset complete")
