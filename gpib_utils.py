# gpib_utils.py
def check_eoi(channel):
    if channel.eoi == 1:
        print("End of Initiation (EOI) detected.")
        return True
    return False

def wait_for_dav(channel):
    while channel.dav == 0:
        pass
    print("Data valid signal (DAV) received.")
