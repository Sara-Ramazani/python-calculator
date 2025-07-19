class History:

    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def show_history(self):
        if not self.records:
            print("No history yet.")
        else:
            for record in self.records:
                print(record)

    def clear_history(self):
        self.records.clear()

