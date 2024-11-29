import cocotb
from cocotb.triggers import RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock
import random

# Define a function to generate a random 8-bit data value
def generate_random_data():
    return random.randint(0, 255)
        


async def run_gpib_transaction(dut, data_in, send_data):
    print("Running GPIB transaction...")
    # Initialize signals
    dut.send_data.value = send_data
    dut.data_in.value = data_in

    # Wait for the next clock edge
    await RisingEdge(dut.clk)
    print("Clock edge detected...")

    # Add a print statement to check the DAV signal

