# gpib_test.py
import cocotb
from cocotb.regression import TestFactory
from cocotb.result import TestSuccess, TestFailure
from gpib_master import GPIBMaster
from gpib_slave import GPIBSlave
from gpib_scoreboard import GPIBScoreboard
from gpib_reset import GPIBReset
from gpib_constants import *

# Driver function to stimulate the GPIB master
class GPIBDriver:
    def __init__(self, dut):
        self.dut = dut
        self.master = GPIBMaster()

    def send_command(self, command):
        """Drive command to the GPIB interface."""
        self.master.initiate(command)

# Monitor to capture the signals from the DUT and compare with expected behavior
class GPIBMonitor:
    def __init__(self, dut, scoreboard):
        self.dut = dut
        self.scoreboard = scoreboard
        self.slave = GPIBSlave()

    async def monitor_signals(self):
        """Monitor the signals and compare with expected output."""
        while True:
            # Listen for commands and check if slave receives correct data
            command = self.slave.listen()
            if command is not None:
                print(f"Slave received command: {hex(command)}")
                self.scoreboard.compare([command])

# Test case to check the GPIB communication
@cocotb.coroutine
async def test_gpib_protocol(dut):
    # Reset the GPIB system
    reset = GPIBReset()
    reset.reset_all()

    # Initialize the scoreboard
    scoreboard = GPIBScoreboard()

    # Create driver and monitor instances
    driver = GPIBDriver(dut)
    monitor = GPIBMonitor(dut, scoreboard)

    # Start monitoring in the background
    cocotb.start_soon(monitor.monitor_signals())

    # Test 1: Master sends a write command
    print("Test 1: Master sends a write command.")
    driver.send_command(COMMAND_WRITE)
    await cocotb.clock.pause()  # Wait for any changes

    # Test 2: Master sends a read command
    print("Test 2: Master sends a read command.")
    driver.send_command(COMMAND_READ)
    await cocotb.clock.pause()

    # Test 3: Verify the scoreboard
    print("Test 3: Verifying the scoreboard.")
    scoreboard.add_expected_data(COMMAND_WRITE)
    scoreboard.add_expected_data(COMMAND_READ)

    # Check if the transactions are correctly compared
    try:
        scoreboard.compare([COMMAND_WRITE, COMMAND_READ])
        print("Test Passed")
    except:
        print("Test Failed")
        raise TestFailure("Scoreboard comparison failed")

# Register the test with the test factory
factory = TestFactory(test_gpib_protocol)
factory.generate_tests()
