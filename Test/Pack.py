class Pack:
    def __init__(self, header, data, target, origin = "", path = "N"):
        self.path = path
        self.header = header
        self.data = data
        self.target = target
        self.origin = origin


