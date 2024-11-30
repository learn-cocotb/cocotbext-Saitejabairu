import cocotb
from cocotb.regression import TestFactory
from cocotb.regression import TestStatus
from cocotb.regression import TestResult
from cocotb.clock import Clock

# Command values for GPIB
COMMAND_WRITE = 0x1

class GPIBDriver:
    def __init__(self, dut, clock, reset):
        self.dut = dut
        self.clock = clock
                self.reset = reset
    
    async def send_command(self, command):
        self.dut.atn.value = 0  # Assert attention
        self.dut.gpib_data.value = command
        self.dut.dav.value = 1  # Data valid
        print(f"Driver: Sending command {hex(command)}")
        await Timer(60, units="ns")
        self.dut.dav.value = 0  # Clear data valid


    async def reset_device(self):
        print("Performing reset...")
        self.dut.reset <= 1
        await cocotb.clock.cycles(5)  # Hold reset for 5 cycles
        self.dut.reset <= 0
        await cocotb.clock.cycles(5)  # Wait for reset to complete
        print("Reset completed.")


