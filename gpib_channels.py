# gpib_channels.py
class GPIBChannel:
    def __init__(self):
        self.dav = 0  # Data valid signal
        self.atn = 0  # Attention signal
        self.eoi = 0  # End of initiation signal
        self.data = 0  # Data bus

    def clear(self):
        self.dav = 0
        self.atn = 0
        self.eoi = 0
        self.data = 0
