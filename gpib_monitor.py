import cocotb
from cocotb.regression import TestFactory

class GPIBMonitor:
    def __init__(self, dut):
        self.dut = dut

    async def capture_transaction(self):
        while True:
            if self.dut.command.value != 0:
                print(f"Captured command: {hex(self.dut.command.value)}")
                # Capture the transaction and compare with expected
                await cocotb.wait(1)  # Wait for some cycles to process the transaction
            await cocotb.clock.cycles(1)  # Pause for 1 clock cycle before checking again
