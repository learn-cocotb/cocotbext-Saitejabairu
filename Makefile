# Makefile for GPIB simulation with cocotb

# Simulation tool
SIM ?= icarus

# Top-level module and test module
TOPLEVEL := gpib_interface
MODULE := gpib_test

# Verilog sources
VERILOG_SOURCES := gpib_interface.v

# Optional: Set the top-level language (Verilog in this case)
TOPLEVEL_LANG ?= verilog

# Optional: Reduce log verbosity for debugging
export COCOTB_REDUCED_LOG_FMT=1

# Include cocotb's default Makefile.sim
include $(shell cocotb-config --makefiles)/Makefile.sim
