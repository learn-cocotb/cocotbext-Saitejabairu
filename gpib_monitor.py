class GPIBMonitor:
    def __init__(self, dut):
        self.dut = dut
        self.received_commands = []
        self.capture_commands = False

    async def monitor_signals(self):
        while True:
            # Wait for rising edge of clock
            await RisingEdge(self.dut.clk)
            # Debugging print to monitor signal states
            print(f"Monitor: clk={self.dut.clk.value}, listener={self.dut.listener.value}, dav={self.dut.dav.value}")
            # Check if the capture_commands flag is set
            if self.capture_commands:
                # Monitor the condition when listener and dav are high
                if self.dut.listener.value == 1 and self.dut.dav.value == 1:
                    command = self.dut.gpib_data.value.integer
                    self.received_commands.append(command)
                    print(f"Monitor: Captured command {hex(command)}")
