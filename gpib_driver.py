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
        print(f"Sending command: {hex(command)}")
        self.dut.command <= command  # Assuming the signal to send the command is called 'command'
        await cocotb.clock.cycles(10)  # Wait for a few cycles to propagate
        print(f"Command {hex(command)} sent successfully")

    async def reset_device(self):
        print("Performing reset...")
        self.dut.reset <= 1
        await cocotb.clock.cycles(5)  # Hold reset for 5 cycles
        self.dut.reset <= 0
        await cocotb.clock.cycles(5)  # Wait for reset to complete
        print("Reset completed.")
