class Pack:
    def __init__(self, path,header, data):
        self.path = path
        self.header = header
        self.data = data

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path

    def get_header(self):
        return self.header

    def get_data(self):
        return self.data