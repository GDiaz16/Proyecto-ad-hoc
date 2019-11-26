class RAM_distributed:
    def __init__(self):
        self.memory = {}
        self.count = 0


    def save(self, data, address):
        n = address % 6 + 1
        device = "N"+ str(n)
