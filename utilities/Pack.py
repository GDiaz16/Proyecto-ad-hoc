class Pack:
    def __init__(self, path,type_m, data):
        self.path = path
        self.type_m = type_m
        self.data = data

    def get_path(self):
        return self.path

    def get_type_m(self):
        return self.type_m

    def get_data(self):
        return self.data