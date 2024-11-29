# gpib_scoreboard.py
class GPIBScoreboard:
    def __init__(self):
        self.expected_data = []

    def add_expected_data(self, data):
        self.expected_data.append(data)

    def compare(self, actual_data):
        for i, expected in enumerate(self.expected_data):
            if expected != actual_data[i]:
                print(f"Mismatch at index {i}: Expected {expected}, got {actual_data[i]}")
            else:
                print(f"Data match at index {i}: {expected}")
