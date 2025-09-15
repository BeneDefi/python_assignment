class Array:
    def __init__(self):
        self.data = []

    def append(self, item):
        self.data += [item]

    def remove(self, item):
        for i in range(len(self.data)):
            if self.data[i] == item:
                self.data = self.data[:i] + self.data[i+1:]
                return

    def insert(self, index, item):
        if index < 0:
            index = max(0, len(self.data) + index)
        if index > len(self.data):
            index = len(self.data)
        self.data = self.data[:index] + [item] + self.data[index:]

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"Array({self.data})"
